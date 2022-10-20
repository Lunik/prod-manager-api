
class RestObject:
  def __init__(self, manager, identifier, **attrs):
    self.manager = manager
    self.identifier = identifier

    self.attrs = attrs

  def __repr__(self):
    if self.identifier:
      return f"<{self.__class__.__name__}({self.manager.name.capitalize()}) /{self.manager.path}/{self.identifier}>"

    return f"<{self.__class__.__name__}({self.manager.name.capitalize()}) /{self.manager.path}>"

  def __getattr__(self, name):
    if name in self.attrs:
      return self.attrs[name]

    if self.identifier:
      return RestManager(self.manager.client, name, f"{self.manager.path}/{self.identifier}/{name}")

    return RestManager(self.manager.client, name, f"{self.manager.path}/{name}")

  def update(self, **attributes):
    return self.manager.update(self, attributes)

  def delete(self):
    self.manager.delete(self)


class RestManager:
  def __init__(self, client, name, path):
    self.client = client
    self.name = name
    self.path = path

  def __repr__(self):
    return f"<{self.__class__.__name__}({self.name.capitalize()}) /{self.path}>"

  def __getattr__(self, name):
    return RestManager(self.client, name, f"{self.path}/{name}")

  def __call__(self):
    res = self.client.make_request(self.path,
      method="GET"
    )

    item = res.json()
    return RestObject(self, None, **item)

  def list(self, **kwargs):
    if 'page' not in kwargs:
      kwargs['page'] = 1

    max_page = 1

    while kwargs['page'] <= max_page:
      res = self.client.make_request(self.path,
        method="GET",
        params=kwargs
      )

      for item in res.json()['items']:
        yield RestObject(self, item['id'], **item)

      max_page = int(res.headers.get('x-total-pages'))
      kwargs['page'] += 1

  def get(self, identifier):
    res = self.client.make_request(f"{self.path}/{identifier}",
      method="GET"
    )

    item = res.json()
    return RestObject(self, item['id'], **item)

  def count(self):
    res = self.client.make_request(self.path,
        method="GET",
        params=dict(per_page=0)
      )

    return int(res.headers.get('x-total'))

  def create(self, **kwargs):
    res = self.client.make_request(f"{self.path}/create",
      method="POST",
      data=kwargs
    )

    item = res.json()
    return RestObject(self, item['id'], **item)

  def update(self, resource, attributes):
    attrs = {**resource.attrs, **attributes}
    res = self.client.make_request(f"{self.path}/{resource.id}/update",
      method="POST",
      data=attrs
    )

    item = res.json()
    return RestObject(self, item['id'], **item)

  def delete(self, resource):
    self.client.make_request(f"{self.path}/{resource.id}/delete",
      method="POST"
    )
