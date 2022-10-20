# Getting started with the API

## `prodmanager.ProdManager` class

To connect to a ProdManager instance, create a `prodmanager.ProdManager` object :

```python
from prodmanager import ProdManager

# anonymous read-only access for public resources
pm = ProdManager("https://prodmanager.example.org")

# api token authentication
pm = ProdManager("https://prodmanager.example.org", token)
```

## Managers

The `prodmanager.ProdManager` class provides managers to access the ProdManager resources. Each manager provides a set of methods to act on the resources. The available methods depend on the resource type.

Examples:

```python
# list all the scopes
scopes = pm.scope.list()
for scope in scopes:
    print(scope)

# get the service with id == 2
service = pm.service.get(2)
print(service)
```

!!! warning

    Calling `list()` will not return the complete list of items. A Python iterator is returned instead. See the Pagination section for more information.

The attributes of objects are defined upon object creation, and depend on the ProdManger API itself. To list the available information associated with an object directly try to access its attributes :

```python
monitor = pm.monitor.get(1)
print(monitor.status)
```

Some objects also provide managers to access related ProdManager resources :

```python
weather = pm.weather.incident()
print(weather)
```

`prod-manager` allows to send any data to the ProdManager server when making queries :

```python
incidents = pm.incident.list(status=['active', 'investigating'])
for incident in incidents:
  print(incident)
```

In case of invalid or missing arguments `prod-manager` will raise an exception with the ProdManager server error message :

```python
pm.scope.create(name="s1")
...
Exception: (400, {'message': 'Scope creation failed', 'reasons': {'name': ['Field must be at least 3 characters long.']}})
```

## Base types

The `prod-manager` package provides some base types.

- `prodmanager.ProdManager` is the primary class, handling the HTTP requests. It holds the ProdManager URL and authentication information.
- `prodmanager.base.RestObject` is the base class for all the ProdManager objects. These objects provide an abstraction for ProdManager resources (scopes, services, and so on).
- `prodmanager.base.RestManager` is the base class for objects managers, providing the API to manipulate the resources and their attributes.
