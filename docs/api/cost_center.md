# Cost Center API

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
const getCostCenter = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Cost Center/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getCostCenters = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'cost_center_name', 'company']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Cost Center?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createCostCenter = async (costCenterData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Cost Center`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(costCenterData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateCostCenter = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Cost Center/${name}`,
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
const deleteCostCenter = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Cost Center/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
