# Retail Cutting Sale API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/resource/Retail Cutting Sale/{name}",
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
    "https://your-site.com/api/resource/Retail Cutting Sale",
    params={
        'fields': '["name","roll_number","cut_qty","grand_total","sale_type","status","posting_date"]',
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
    "https://your-site.com/api/resource/Retail Cutting Sale",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "roll_number": "ROLL-001",
        "cut_qty": 10.0,
        "rate": 35.0,
        "sale_type": "Cash",
        "posting_date": "2024-01-20"
    }
)
```

## PUT

```python
import requests

response = requests.put(
    "https://your-site.com/api/resource/Retail Cutting Sale/{name}",
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
    "https://your-site.com/api/resource/Retail Cutting Sale/{name}",
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
    "https://your-site.com/api/resource/Retail Cutting Sale/{name}/submit",
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
    "https://your-site.com/api/resource/Retail Cutting Sale/{name}/cancel",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
