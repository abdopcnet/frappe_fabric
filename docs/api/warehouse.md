# Warehouse API

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
const getWarehouse = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Warehouse/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getWarehouses = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'warehouse_name', 'company']),
    filters: JSON.stringify(filters.length ? filters : [['is_group', '=', 0]]),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Warehouse?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createWarehouse = async (warehouseData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Warehouse`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(warehouseData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateWarehouse = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Warehouse/${name}`,
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
const deleteWarehouse = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Warehouse/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
