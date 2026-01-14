# API Reference

Frappe Fabric Management API endpoints.

## Authentication

All requests require API key authentication:

```
Authorization: token {API_KEY}:{API_SECRET}
Content-Type: application/json
```

## Roll APIs

### GET /api/method/frappe_fabric.api.roll.get_roll

Get roll details by roll number.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| roll_number | string | Yes | Roll number |

**Response:**
```json
{
  "message": {
    "roll_number": "ROLL-20240115-0001-ABCD",
    "item_code": "FAB-001",
    "item_name": "Cotton Fabric White",
    "current_length": 45.0,
    "warehouse": "Main Warehouse",
    "status": "Available"
  }
}
```

### POST /api/method/frappe_fabric.api.roll.search_rolls

Search rolls.

**Body:**
```json
{
  "filters": {
    "item_code": "FAB-001",
    "warehouse": "Main Warehouse",
    "status": "Available",
    "min_length": 10
  },
  "page": 1,
  "page_size": 20
}
```

## Receipt APIs

### POST /api/method/frappe_fabric.api.receipt.create_container_receipt

Create new container receipt.

**Body:**
```json
{
  "data": {
    "container_number": "CONT-1001",
    "supplier": "SUP-001",
    "warehouse": "Main Warehouse",
    "expected_items": [
      {
        "item_code": "FAB-001",
        "expected_rolls": 100,
        "expected_meters": 5000
      }
    ]
  }
}
```

### POST /api/method/frappe_fabric.api.receipt.scan_roll

Scan/add roll to receipt.

**Body:**
```json
{
  "receipt_no": "CR-2024-0001",
  "roll_data": {
    "item_code": "FAB-001",
    "color": "White",
    "scanned_length": 50.5,
    "bin_location": "A-01-02"
  }
}
```

## Cutting APIs

### POST /api/method/frappe_fabric.api.cutting.create_sample_cutting

Create sample cutting.

**Body:**
```json
{
  "data": {
    "warehouse": "Main Warehouse",
    "purpose": "Customer Sample",
    "expense_account": "Sample Cutting Expenses - TC",
    "items": [
      {
        "roll_number": "ROLL-20240115-0001-ABCD",
        "cut_qty": 2.5
      }
    ],
    "submit": true
  }
}
```

### POST /api/method/frappe_fabric.api.cutting.create_retail_sale

Create retail sale.

**Body:**
```json
{
  "data": {
    "roll_number": "ROLL-20240115-0001-ABCD",
    "cut_qty": 5.0,
    "rate": 25.00,
    "sale_type": "Cash",
    "submit": true
  }
}
```

## Reports APIs

### POST /api/method/frappe_fabric.api.reports.get_stock_balance

Stock balance report.

**Body:**
```json
{
  "filters": {
    "item_code": "FAB-001",
    "warehouse": "Main Warehouse"
  }
}
```

---

**Updated:** January 2024
**Version:** 1.0.0
