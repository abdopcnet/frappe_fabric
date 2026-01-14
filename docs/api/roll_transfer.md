# Roll Transfer API

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
const getRollTransfer = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Transfer/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getRollTransfers = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'from_warehouse', 'to_warehouse', 'status', 'posting_date']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Transfer?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createRollTransfer = async (transferData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Transfer`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(transferData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateRollTransfer = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Transfer/${name}`,
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
const deleteRollTransfer = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Transfer/${name}`,
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
const submitRollTransfer = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Transfer/${name}/submit`,
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
const cancelRollTransfer = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Transfer/${name}/cancel`,
    {
      method: 'POST',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
