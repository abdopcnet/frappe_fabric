# Fabric Roll API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Fabric Roll/{name}",
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
    "https://your-site.com/api/resource/Fabric Roll",
    params={
        'fields': '["name","roll_number","item_code","current_length","warehouse","status"]',
        'filters': '[["is_active","=",1]]',
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
    "https://your-site.com/api/resource/Fabric Roll",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "roll_number": "ROLL-001",
        "item_code": "FAB-001",
        "color": "WHITE",
        "original_length": 100.0,
        "warehouse": "Main Warehouse"
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Fabric Roll/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "warehouse": "New Warehouse",
        "bin_location": "A-01-05"
    }
)
```

## DELETE

```python
import requests

response = requests.delete(
    "https://your-site.com/api/resource/Fabric Roll/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
