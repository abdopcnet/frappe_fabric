# API Tree Structure

Complete API endpoint structure for Frappe Fabric Management application.

## API Organization

All APIs are organized by function in the `frappe_fabric/api/` module.

## API Modules

### 1. Roll APIs (api/roll.py)

Roll management and tracking endpoints.

**Endpoints:**

| Method | Endpoint | Function | Description |
|--------|----------|----------|-------------|
| GET | `/api/method/frappe_fabric.api.roll.get_roll` | `get_roll(roll_number)` | Get roll details by roll number |
| GET | `/api/method/frappe_fabric.api.roll.get_roll_by_qr` | `get_roll_by_qr(qr_code)` | Get roll by QR code scan |
| POST | `/api/method/frappe_fabric.api.roll.search_rolls` | `search_rolls(filters, search_term, page, page_size)` | Search rolls with filters and pagination |
| POST | `/api/method/frappe_fabric.api.roll.update_roll_location` | `update_roll_location(roll_number, warehouse, bin_location)` | Update roll warehouse location |
| POST | `/api/method/frappe_fabric.api.roll.reserve_roll` | `reserve_roll(roll_number, reserve_length, reference_doctype, reference_name)` | Reserve quantity from a roll |

### 2. Receipt APIs (api/receipt.py)

Container receipt management endpoints.

**Endpoints:**

| Method | Endpoint | Function | Description |
|--------|----------|----------|-------------|
| POST | `/api/method/frappe_fabric.api.receipt.create_container_receipt` | `create_container_receipt(data)` | Create a new container receipt |
| GET | `/api/method/frappe_fabric.api.receipt.get_container_receipt` | `get_container_receipt(receipt_no)` | Get container receipt details |
| POST | `/api/method/frappe_fabric.api.receipt.scan_roll` | `scan_roll(receipt_no, roll_data)` | Scan/add a roll to the receipt |

### 3. Cutting APIs (api/cutting.py)

Sample cutting and retail sales endpoints.

**Endpoints:**

| Method | Endpoint | Function | Description |
|--------|----------|----------|-------------|
| POST | `/api/method/frappe_fabric.api.cutting.create_sample_cutting` | `create_sample_cutting(data)` | Create a sample cutting document |
| POST | `/api/method/frappe_fabric.api.cutting.create_retail_sale` | `create_retail_sale(data)` | Create a retail cutting sale |

### 4. Reports APIs (api/reports.py)

Reporting and analytics endpoints.

**Endpoints:**

| Method | Endpoint | Function | Description |
|--------|----------|----------|-------------|
| POST | `/api/method/frappe_fabric.api.reports.get_stock_balance` | `get_stock_balance(filters)` | Get roll stock balance report |
| POST | `/api/method/frappe_fabric.api.reports.get_movement_history` | `get_movement_history(filters)` | Get roll movement history |
| POST | `/api/method/frappe_fabric.api.reports.get_cutting_summary` | `get_cutting_summary(filters)` | Get cutting summary report |

## API Endpoint Summary

### GET Operations (Retrieve Data)
- `get_roll` - Get single roll
- `get_roll_by_qr` - Get roll by QR code
- `get_container_receipt` - Get container receipt
- `search_rolls` - Search/filter rolls (with pagination)

### CREATE Operations
- `create_container_receipt` - Create container receipt
- `create_sample_cutting` - Create sample cutting
- `create_retail_sale` - Create retail sale
- `scan_roll` - Scan/add roll to receipt

### UPDATE Operations
- `update_roll_location` - Update roll warehouse location
- `reserve_roll` - Reserve roll quantity

### REPORT Operations
- `get_stock_balance` - Stock balance report
- `get_movement_history` - Movement history report
- `get_cutting_summary` - Cutting summary report

## API Authentication

All APIs require authentication via API Key:

```
Authorization: token {API_KEY}:{API_SECRET}
Content-Type: application/json
```

## Response Format

All APIs return JSON responses in Frappe's standard format:

**Success:**
```json
{
  "message": {
    // Response data
  }
}
```

**Error:**
```json
{
  "exc_type": "ValidationError",
  "exc": "Error message",
  "exception": "frappe.exceptions.ValidationError"
}
```

## Detailed Documentation

For detailed API documentation, see:

- [Roll APIs](docs/api/roll.md)
- [Receipt APIs](docs/api/receipt.md)
- [Cutting APIs](docs/api/cutting.md)
- [Reports APIs](docs/api/reports.md)
