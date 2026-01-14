# Cutting & Sales API

## POST

```python
import requests

response = requests.post(
    "https://your-site.com/api/method/frappe_fabric.api.cutting.create_sample_cutting",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "warehouse": "Main Warehouse",
        "purpose": "Customer Sample",
        "items": []
    }
)
```

## POST

```python
import requests

response = requests.post(
    "https://your-site.com/api/method/frappe_fabric.api.cutting.create_retail_sale",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "roll_number": "ROLL-001",
        "cut_qty": 10.0,
        "rate": 35.0,
        "sale_type": "Cash"
    }
)
```
