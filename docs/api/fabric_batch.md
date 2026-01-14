# Fabric Batch API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Fabric Batch/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```

## GET_MANY

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Fabric Batch",
    params={
        'fields': '["name","batch_id","item_code","manufacturing_date"]',
        'limit_page_length': 100
    },
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```

## POST

```python
import requests

response = requests.post(
    "https://your-site.com/api/resource/Fabric Batch",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "batch_id": "BATCH-001",
        "item_code": "FAB-001",
        "manufacturing_date": "2024-01-15"
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Fabric Batch/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "expiry_date": "2025-01-15"
    }
)
```

## DELETE

```python
import requests

response = requests.delete(
    "https://your-site.com/api/resource/Fabric Batch/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
