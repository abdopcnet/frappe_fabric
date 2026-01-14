# Warehouse API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Warehouse/{name}",
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
    "https://your-site.com/api/resource/Warehouse",
    params={
        'fields': '["name","warehouse_name","company"]',
        'filters': '[["is_group","=",0]]',
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
    "https://your-site.com/api/resource/Warehouse",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "warehouse_name": "Fabric Warehouse",
        "company": "Your Company",
        "is_group": 0
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Warehouse/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "warehouse_name": "Updated Warehouse Name"
    }
)
```

## DELETE

```python
import requests

response = requests.delete(
    "https://your-site.com/api/resource/Warehouse/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
