# Container Receipt API

Frappe Fabric Management Container Receipt APIs.

## Authentication

All requests require API key authentication:

```
Authorization: token {API_KEY}:{API_SECRET}
Content-Type: application/json
```

## Setup

```javascript
const ERPNEXT_URL = import.meta.env.VITE_ERPNEXT_URL || 'https://your-site.com';
const API_KEY = import.meta.env.VITE_ERPNEXT_API_KEY;
const API_SECRET = import.meta.env.VITE_ERPNEXT_API_SECRET;

const headers = {
  'Authorization': `token ${API_KEY}:${API_SECRET}`,
  'Content-Type': 'application/json'
};
```

## POST /api/method/frappe_fabric.api.receipt.create_container_receipt

Create new container receipt.

**Body:**
```json
{
  "data": {
    "container_number": "CONT-1001",
    "supplier": "SUP-001",
    "warehouse": "Main Warehouse",
    "posting_date": "2024-01-15",
    "expected_items": [
      {
        "item_code": "FAB-001",
        "expected_rolls": 100,
        "expected_meters": 5000,
        "color": "WHITE"
      }
    ]
  }
}
```

**React Example:**
```javascript
const createContainerReceipt = async (receiptData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.receipt.create_container_receipt`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ data: receiptData })
    }
  );
  const data = await response.json();
  return data.message;
};
```

## GET /api/method/frappe_fabric.api.receipt.get_container_receipt

Get container receipt details.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| receipt_no | string | Yes | Receipt document name |

**React Example:**
```javascript
const getContainerReceipt = async (receiptNo) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.receipt.get_container_receipt?receipt_no=${receiptNo}`,
    { headers }
  );
  const data = await response.json();
  return data.message;
};
```

## POST /api/method/frappe_fabric.api.receipt.scan_roll

Scan/add roll to receipt.

**Body:**
```json
{
  "receipt_no": "CR-2024-0001",
  "roll_data": {
    "item_code": "FAB-001",
    "color": "WHITE",
    "scanned_length": 50.5,
    "bin_location": "A-01-02"
  }
}
```

**React Example:**
```javascript
const scanRoll = async (receiptNo, rollData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.receipt.scan_roll`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ receipt_no: receiptNo, roll_data: rollData })
    }
  );
  const data = await response.json();
  return data.message;
};
```

---

**Updated:** January 2024
**Version:** 1.0.0
