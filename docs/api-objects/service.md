# Service

## Examples

### List services

```python
services = pm.service.list()
```

### Get a single service

```python
# Get a service by ID
service_id = 11
service = pm.service.get(service_id)
```

### Create a service

```python
service = pm.service.create(
  name="My service",
  description="Demonstration service",
)
```

### Updating a service

```python
service = service.update(
  description="Updated service description",
)
```

### Deleting a service

```python
service.delete()
```