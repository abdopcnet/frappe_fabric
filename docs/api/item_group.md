# Item Group API

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
const getItemGroup = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Item Group/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getItemGroups = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'item_group_name', 'parent_item_group']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Item Group?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createItemGroup = async (itemGroupData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Item Group`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(itemGroupData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateItemGroup = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Item Group/${name}`,
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
const deleteItemGroup = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Item Group/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
