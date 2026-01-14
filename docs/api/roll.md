# Roll Management API

Frappe Fabric Management Roll APIs.

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

## GET /api/method/frappe_fabric.api.roll.get_roll

Get roll details by roll number.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| roll_number | string | Yes | Roll number |

**React Example:**
```javascript
const getRoll = async (rollNumber) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.roll.get_roll?roll_number=${rollNumber}`,
    { headers }
  );
  const data = await response.json();
  return data.message;
};
```

**Response:**
```json
{
  "message": {
    "roll_number": "ROLL-20240115-0001-ABCD",
    "item_code": "FAB-001",
    "item_name": "Cotton Fabric White",
    "color": "WHITE",
    "current_length": 45.0,
    "warehouse": "Main Warehouse",
    "status": "Available",
    "movements": []
  }
}
```

## GET /api/method/frappe_fabric.api.roll.get_roll_by_qr

Get roll by QR code scan.

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| qr_code | string | Yes | QR code value |

**React Example:**
```javascript
const getRollByQR = async (qrCode) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.roll.get_roll_by_qr?qr_code=${qrCode}`,
    { headers }
  );
  const data = await response.json();
  return data.message;
};
```

## POST /api/method/frappe_fabric.api.roll.search_rolls

Search rolls with filters and pagination.

**Body:**
```json
{
  "filters": {
    "item_code": "FAB-001",
    "warehouse": "Main Warehouse",
    "status": "Available",
    "min_length": 10
  },
  "search_term": "ROLL",
  "page": 1,
  "page_size": 20
}
```

**React Example:**
```javascript
const searchRolls = async (filters, searchTerm, page = 1, pageSize = 20) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.roll.search_rolls`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ filters, search_term: searchTerm, page, page_size: pageSize })
    }
  );
  const data = await response.json();
  return data.message;
};
```

## POST /api/method/frappe_fabric.api.roll.update_roll_location

Update roll warehouse location.

**Body:**
```json
{
  "roll_number": "ROLL-001",
  "warehouse": "Main Warehouse",
  "bin_location": "A-01-05"
}
```

**React Example:**
```javascript
const updateRollLocation = async (rollNumber, warehouse, binLocation) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.roll.update_roll_location`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({
        roll_number: rollNumber,
        warehouse: warehouse,
        bin_location: binLocation
      })
    }
  );
  const data = await response.json();
  return data.message;
};
```

## POST /api/method/frappe_fabric.api.roll.reserve_roll

Reserve quantity from a roll.

**Body:**
```json
{
  "roll_number": "ROLL-001",
  "reserve_length": 10.0,
  "reference_doctype": "Sales Order",
  "reference_name": "SO-001"
}
```

**React Example:**
```javascript
const reserveRoll = async (rollNumber, reserveLength, referenceDoctype, referenceName) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.roll.reserve_roll`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({
        roll_number: rollNumber,
        reserve_length: reserveLength,
        reference_doctype: referenceDoctype,
        reference_name: referenceName
      })
    }
  );
  const data = await response.json();
  return data.message;
};
```

---

**Updated:** January 2024
**Version:** 1.0.0
