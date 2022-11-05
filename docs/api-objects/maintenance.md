# Maintenance

## Examples

### List maintenances

```python
maintenances = pm.maintenance.list()
```

### Get a single maintenance

```python
# Get a maintenance by ID
maintenance_id = 11
maintenance = pm.maintenance.get(maintenance_id)
```

### Create a maintenance

```python
maintenance = pm.maintenance.create(
  name="My maintenance",
  description="Demonstration maintenance",
  service=service.id,
  scope=scope.id,
  service_status="degraded",
)
```

### Updating a maintenance

```python
maintenance = maintenance.update(
  status="in-progress",
)
```

### Deleting a maintenance

```python
maintenance.delete()
```