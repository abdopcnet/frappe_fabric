# Sample Cutting API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Sample Cutting/{name}",
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
    "https://your-site.com/api/resource/Sample Cutting",
    params={
        'fields': '["name","warehouse","purpose","total_cut_qty","status","posting_date"]',
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
    "https://your-site.com/api/resource/Sample Cutting",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "warehouse": "Main Warehouse",
        "purpose": "Customer Sample",
        "posting_date": "2024-01-20",
        "items": []
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Sample Cutting/{name}",
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
    "https://your-site.com/api/resource/Sample Cutting/{name}",
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
    "https://your-site.com/api/resource/Sample Cutting/{name}/submit",
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
    "https://your-site.com/api/resource/Sample Cutting/{name}/cancel",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
