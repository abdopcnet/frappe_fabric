# Fabric Batch API

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
const getFabricBatch = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Batch/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getFabricBatches = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'batch_id', 'item_code', 'manufacturing_date']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Batch?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createFabricBatch = async (batchData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Batch`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(batchData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateFabricBatch = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Batch/${name}`,
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
const deleteFabricBatch = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Fabric Batch/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
