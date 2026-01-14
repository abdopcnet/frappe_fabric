# Account API

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
const getAccount = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Account/${name}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## GET_MANY

```javascript
const getAccounts = async (filters = []) => {
  const params = new URLSearchParams({
    fields: JSON.stringify(['name', 'account_name', 'account_type']),
    filters: JSON.stringify(filters),
    limit_page_length: 100
  });
  
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Account?${params}`,
    { headers }
  );
  const data = await response.json();
  return data.data;
};
```

## POST

```javascript
const createAccount = async (accountData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Account`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify(accountData)
    }
  );
  const data = await response.json();
  return data.data;
};
```

## PUT

```javascript
const updateAccount = async (name, updateData) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Account/${name}`,
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
const deleteAccount = async (name) => {
  const response = await fetch(
    `${ERPNEXT_URL}/api/resource/Account/${name}`,
    {
      method: 'DELETE',
      headers
    }
  );
  const data = await response.json();
  return data;
};
```
