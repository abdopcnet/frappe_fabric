# Container Receipt API

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
const getContainerReceipt = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Container Receipt/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getContainerReceipts = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'container_number', 'supplier', 'status', 'posting_date']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Container Receipt?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createContainerReceipt = async (receiptData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Container Receipt`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(receiptData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateContainerReceipt = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Container Receipt/${name}`,
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
const deleteContainerReceipt = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Container Receipt/${name}`,
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
const submitContainerReceipt = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Container Receipt/${name}/submit`,
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
const cancelContainerReceipt = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Container Receipt/${name}/cancel`,
    {
      method: 'POST',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
