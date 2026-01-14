# Customer API

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
const getCustomer = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Customer/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getCustomers = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'customer_name', 'customer_type']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Customer?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createCustomer = async (customerData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Customer`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(customerData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateCustomer = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Customer/${name}`,
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
const deleteCustomer = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Customer/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
