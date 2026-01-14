# Sample Cutting API

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
const getSampleCutting = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sample Cutting/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getSampleCuttings = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'warehouse', 'purpose', 'total_cut_qty', 'status', 'posting_date']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sample Cutting?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createSampleCutting = async (cuttingData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sample Cutting`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(cuttingData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateSampleCutting = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sample Cutting/${name}`,
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
const deleteSampleCutting = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sample Cutting/${name}`,
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
const submitSampleCutting = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sample Cutting/${name}/submit`,
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
const cancelSampleCutting = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Sample Cutting/${name}/cancel`,
    {
      method: 'POST',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
