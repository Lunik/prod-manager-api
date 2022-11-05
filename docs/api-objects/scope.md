# Scope

## Examples

### List scopes

```python
scopes = pm.scope.list()
```

### Get a single scope

```python
# Get a scope by ID
scope_id = 17
scope = pm.scope.get(scope_id)
```

### Create a scope

```python
scope = pm.scope.create(
  name="My scope",
  description="Demonstration scope",
)
```

### Updating a scope

```python
scope = scope.update(
  description="Updated scope description",
)
```

### Deleting a scope

```python
scope.delete()
```