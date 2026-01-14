# Reports API

Frappe Fabric Management Reports APIs.

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

## POST /api/method/frappe_fabric.api.reports.get_stock_balance

Get roll stock balance report.

**Body:**
```json
{
  "filters": {
    "warehouse": "Main Warehouse",
    "item_code": "FAB-001"
  }
}
```

**React Example:**
```javascript
const getStockBalance = async (filters) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.reports.get_stock_balance`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ filters })
    }
  );
  const data = await response.json();
  return data.message;
};
```

## POST /api/method/frappe_fabric.api.reports.get_movement_history

Get roll movement history.

**Body:**
```json
{
  "filters": {
    "roll_number": "ROLL-001",
    "from_date": "2024-01-01",
    "to_date": "2024-01-31",
    "movement_type": "Consumption"
  }
}
```

**React Example:**
```javascript
const getMovementHistory = async (filters) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.reports.get_movement_history`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ filters })
    }
  );
  const data = await response.json();
  return data.message;
};
```

## POST /api/method/frappe_fabric.api.reports.get_cutting_summary

Get cutting summary report.

**Body:**
```json
{
  "filters": {
    "from_date": "2024-01-01",
    "to_date": "2024-01-31",
    "purpose": "Customer Sample"
  }
}
```

**React Example:**
```javascript
const getCuttingSummary = async (filters) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.reports.get_cutting_summary`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ filters })
    }
  );
  const data = await response.json();
  return data.message;
};
```

---

**Updated:** January 2024
**Version:** 1.0.0
