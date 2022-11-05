# Incident

## Examples

### List incidents

```python
incidents = pm.incident.list()
```

### Get a single incident

```python
# Get a incident by ID
incident_id = 11
incident = pm.incident.get(incident_id)
```

### Create a incident

```python
incident = pm.incident.create(
  name="My incident",
  description="Demonstration incident",
  service=service.id,
  scope=scope.id,
  severity="high",
)
```

### Updating a incident

```python
incident = incident.update(
  status="investigating",
)
```

### Deleting a incident

```python
incident.delete()
```