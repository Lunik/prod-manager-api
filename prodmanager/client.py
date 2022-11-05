from requests import Session

from prodmanager.log import init_logger
from prodmanager.base import RestManager

class ProdManager:
  def __init__(self, url, token=None, session=None, log_level="INFO"):
    self.url = f"{url}/api"

    self.logger = init_logger(level=log_level)

    self.session = session if session else Session()
    if token:
      self.session.headers["Authorization"] = f"Bearer {token}"

  def make_request(self, path, **kwargs):
    kwargs['url'] = f"{self.url}/{path}"

    self.logger.debug("%s %s %s", kwargs['method'], kwargs['url'], kwargs.get('params'))
    response = self.session.request(**kwargs)

    if response.status_code != 200:
      raise Exception(response.status_code, response.json())

    return response

  def __getattr__(self, name):
    return RestManager(self, name, name)
