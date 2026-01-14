# Sales Invoice API

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

## GET

```javascript
const getSalesInvoice = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sales Invoice/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getSalesInvoices = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'customer', 'posting_date', 'grand_total', 'status']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sales Invoice?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createSalesInvoice = async (invoiceData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sales Invoice`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(invoiceData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateSalesInvoice = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sales Invoice/${name}`,
    {
      method: 'PUT',
      headers,
      body: JSON.stringify(updateData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## DELETE

```javascript
const deleteSalesInvoice = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sales Invoice/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```

## SUBMIT

```javascript
const submitSalesInvoice = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sales Invoice/${name}/submit`,
    {
      method: 'POST',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```

## CANCEL

```javascript
const cancelSalesInvoice = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sales Invoice/${name}/cancel`,
    {
      method: 'POST',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
