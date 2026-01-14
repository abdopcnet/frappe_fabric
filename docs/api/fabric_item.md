# Fabric Item API

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
const getFabricItem = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Item/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getFabricItems = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'item_code', 'item_name', 'fabric_type', 'standard_rate']),
    filters: JSON.stringify(filters.length ? filters : [['is_active', '=', 1]]),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Item?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createFabricItem = async (itemData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Item`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(itemData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateFabricItem = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Item/${name}`,
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
const deleteFabricItem = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Item/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
