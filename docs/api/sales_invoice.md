# Sales Invoice API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Sales Invoice/{name}",
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
    "https://your-site.com/api/resource/Sales Invoice",
    params={
        'fields': '["name","customer","posting_date","grand_total","status"]',
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
    "https://your-site.com/api/resource/Sales Invoice",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "customer": "CUST-001",
        "posting_date": "2024-01-20",
        "items": []
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Sales Invoice/{name}",
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
    "https://your-site.com/api/resource/Sales Invoice/{name}",
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
    "https://your-site.com/api/resource/Sales Invoice/{name}/submit",
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
    "https://your-site.com/api/resource/Sales Invoice/{name}/cancel",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
