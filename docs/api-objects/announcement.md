# Announcement

## Examples

### List announcements

```python
announcements = pm.announcement.list()
```

### Get a single announcement

```python
# Get a announcement by ID
announcement_id = 11
announcement = pm.announcement.get(announcement_id)
```

### Create a announcement

```python
announcement = pm.announcement.create(
  name="My announcement",
  description="Demonstration announcement",
  service=service.id,
  scope=scope.id,
  level="medium",
)
```

### Updating a announcement

```python
announcement = announcement.update(
  description="Updated announcement",
  level="low",
)
```

### Deleting a announcement

```python
announcement.delete()
```