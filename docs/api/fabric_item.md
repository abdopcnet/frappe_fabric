# Fabric Item API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Fabric Item/{name}",
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
    "https://your-site.com/api/resource/Fabric Item",
    params={
        'fields': '["name","item_code","item_name","fabric_type","standard_rate"]',
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
    "https://your-site.com/api/resource/Fabric Item",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "item_code": "FAB-001",
        "item_name": "Cotton Fabric White",
        "item_group": "Fabrics",
        "fabric_type": "Cotton",
        "width": 150.0,
        "standard_rate": 30.00
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Fabric Item/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "standard_rate": 35.00
    }
)
```

## DELETE

```python
import requests

response = requests.delete(
    "https://your-site.com/api/resource/Fabric Item/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
