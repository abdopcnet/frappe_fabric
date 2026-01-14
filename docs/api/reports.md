# Reports API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/method/frappe_fabric.api.reports.get_stock_balance",
    params={
        'filters': '{"warehouse": "Main Warehouse", "item_code": "FAB-001"}'
    },
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/method/frappe_fabric.api.reports.get_movement_history",
    params={
        'filters': '{"roll_number": "ROLL-001", "from_date": "2024-01-01", "to_date": "2024-01-31"}'
    },
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/method/frappe_fabric.api.reports.get_cutting_summary",
    params={
        'filters': '{"from_date": "2024-01-01", "to_date": "2024-01-31"}'
    },
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    }
)
```
