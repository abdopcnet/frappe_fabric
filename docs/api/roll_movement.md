# Roll Movement API

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
const getRollMovement = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Movement/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getRollMovements = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'roll_number', 'movement_type', 'quantity', 'warehouse', 'posting_date']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Movement?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createRollMovement = async (movementData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Movement`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(movementData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateRollMovement = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Movement/${name}`,
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
const deleteRollMovement = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Roll Movement/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
