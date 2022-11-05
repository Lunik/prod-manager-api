# Monitor

## Examples

### List monitors

```python
monitors = pm.monitor.list()
```

### Get a single monitor

```python
# Get a monitor by ID
monitor_id = 11
monitor = pm.monitor.get(monitor_id)
```

### Create a monitor

```python
monitor = pm.monitor.create(
  name="My monitor",
  description="Demonstration monitor",
  service=service.id,
  scope=scope.id,
)
```

### Updating a monitor

```python
monitor = monitor.update(
  status="warning",
)
```

### Deleting a monitor

```python
monitor.delete()
```