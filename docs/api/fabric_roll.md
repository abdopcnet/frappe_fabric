# Fabric Roll API

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
const getFabricRoll = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Roll/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getFabricRolls = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'roll_number', 'item_code', 'current_length', 'warehouse', 'status']),
    filters: JSON.stringify(filters.length ? filters : [['is_active', '=', 1]]),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Roll?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createFabricRoll = async (rollData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Roll`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(rollData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateFabricRoll = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Roll/${name}`,
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
const deleteFabricRoll = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Roll/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
