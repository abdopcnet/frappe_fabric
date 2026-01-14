# Item API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Item/{name}",
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
    "https://your-site.com/api/resource/Item",
    params={
        'fields': '["name","item_code","item_name","item_group","is_fabric_item"]',
        'filters': '[["is_fabric_item","=",1]]',
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
    "https://your-site.com/api/resource/Item",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "item_code": "FAB-002",
        "item_name": "Polyester Fabric",
        "item_group": "Fabrics",
        "is_fabric_item": 1,
        "stock_uom": "Meter",
        "is_stock_item": 1
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Item/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "is_fabric_item": 1
    }
)
```

## DELETE

```python
import requests

response = requests.delete(
    "https://your-site.com/api/resource/Item/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
