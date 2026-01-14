# Roll Management API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/method/frappe_fabric.api.roll.get_roll",
    params={
        'roll_number': 'ROLL-001'
    },
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
    "https://your-site.com/api/method/frappe_fabric.api.roll.search_rolls",
    params={
        'filters': '{"item_code": "FAB-001", "warehouse": "Main Warehouse"}',
        'search_term': 'ROLL',
        'page': 1,
        'page_size': 20
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
    "https://your-site.com/api/method/frappe_fabric.api.roll.update_roll_location",
    params={
        'roll_number': 'ROLL-001',
        'warehouse': 'Main Warehouse',
        'bin_location': 'A-01-05'
    },
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```

## PUT

```python
import requests

response = requests.post(
    "https://your-site.com/api/method/frappe_fabric.api.roll.reserve_roll",
    params={
        'roll_number': 'ROLL-001',
        'reserve_length': 10.0,
        'reference_doctype': 'Sales Order',
        'reference_name': 'SO-001'
    },
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
