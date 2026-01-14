# Retail Cutting Sale API

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
const getRetailCuttingSale = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Retail Cutting Sale/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getRetailCuttingSales = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'roll_number', 'cut_qty', 'grand_total', 'sale_type', 'status', 'posting_date']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Retail Cutting Sale?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createRetailCuttingSale = async (saleData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Retail Cutting Sale`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(saleData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateRetailCuttingSale = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Retail Cutting Sale/${name}`,
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
const deleteRetailCuttingSale = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Retail Cutting Sale/${name}`,
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
const submitRetailCuttingSale = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Retail Cutting Sale/${name}/submit`,
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
const cancelRetailCuttingSale = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Retail Cutting Sale/${name}/cancel`,
    {
      method: 'POST',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
