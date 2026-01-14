# Container Receipt API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Container Receipt/{name}",
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
    "https://your-site.com/api/resource/Container Receipt",
    params={
        'fields': '["name","container_number","supplier","status","posting_date"]',
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
    "https://your-site.com/api/resource/Container Receipt",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "container_number": "CONT-001",
        "supplier": "SUP-001",
        "warehouse": "Main Warehouse",
        "posting_date": "2024-01-15"
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Container Receipt/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "remarks": "Updated remarks"
    }
)
```

## DELETE

```python
import requests

response = requests.delete(
    "https://your-site.com/api/resource/Container Receipt/{name}",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```

## SUBMIT

```python
import requests

response = requests.post(
    "https://your-site.com/api/resource/Container Receipt/{name}/submit",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```

## CANCEL

```python
import requests

response = requests.post(
    "https://your-site.com/api/resource/Container Receipt/{name}/cancel",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
