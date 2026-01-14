# Container Receipt API

## GET

```python
import requests

response = requests.get(
    "https://your-site.com/api/method/frappe_fabric.api.receipt.get_container_receipt",
    params={
        'receipt_no': 'REC-001'
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
    "https://your-site.com/api/method/frappe_fabric.api.receipt.create_container_receipt",
    params={},
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "container_number": "CONT-001",
        "supplier": "SUP-001",
        "warehouse": "Main Warehouse",
        "expected_items": []
    }
)
```

## PUT

```python
import requests

response = requests.post(
    "https://your-site.com/api/method/frappe_fabric.api.receipt.scan_roll",
    params={
        'receipt_no': 'REC-001'
    },
    headers={
        'Authorization': 'token {API_KEY}:{API_SECRET}',
        'Content-Type': 'application/json',
    },
    json={
        "item_code": "FAB-001",
        "color": "WHITE",
        "scanned_length": 100.0,
        "bin_location": "A-01-05"
    }
)
```
