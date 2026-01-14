# Supplier API

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
const getSupplier = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Supplier/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getSuppliers = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'supplier_name', 'supplier_type']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Supplier?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createSupplier = async (supplierData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Supplier`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(supplierData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateSupplier = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Supplier/${name}`,
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
const deleteSupplier = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Supplier/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
