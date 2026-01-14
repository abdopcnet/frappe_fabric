# Cutting & Sales API

Frappe Fabric Management Cutting and Sales APIs.

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

## POST /api/method/frappe_fabric.api.cutting.create_sample_cutting

Create sample cutting document.

**Body:**
```json
{
  "data": {
    "warehouse": "Main Warehouse",
    "purpose": "Customer Sample",
    "customer": "CUST-001",
    "expense_account": "Sample Cutting Expenses - TC",
    "cost_center": "Main - TC",
    "posting_date": "2024-01-20",
    "items": [
      {
        "roll_number": "ROLL-20240115-0001-ABCD",
        "cut_qty": 2.5,
        "remarks": "Sample for customer"
      }
    ],
    "submit": true
  }
}
```

**React Example:**
```javascript
const createSampleCutting = async (cuttingData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.cutting.create_sample_cutting`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ data: cuttingData })
    }
  );
  const data = await response.json();
  return data.message;
};
```

## POST /api/method/frappe_fabric.api.cutting.create_retail_sale

Create retail cutting sale.

**Body:**
```json
{
  "data": {
    "roll_number": "ROLL-20240115-0001-ABCD",
    "cut_qty": 5.0,
    "rate": 25.00,
    "sale_type": "Cash",
    "customer": "CUST-001",
    "warehouse": "Main Warehouse",
    "posting_date": "2024-01-20",
    "discount_percentage": 0,
    "tax_amount": 0,
    "submit": true
  }
}
```

**React Example:**
```javascript
const createRetailSale = async (saleData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/method/frappe_fabric.api.cutting.create_retail_sale`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ data: saleData })
    }
  );
  const data = await response.json();
  return data.message;
};
```

---

**Updated:** January 2024
**Version:** 1.0.0
