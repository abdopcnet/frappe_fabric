# Installation Guide

Complete installation and setup guide for Frappe Fabric Management App.

## Requirements

### Software Required:
- Frappe Framework v14 or higher
- ERPNext v14 or higher
- Python 3.10+
- Node.js 18+
- MariaDB 10.6+
- Redis

### Additional Libraries:

```bash
pip install qrcode Pillow
```

## Installation Steps

### Step 1: Copy Files

```bash
# Go to apps directory
cd ~/frappe-bench/apps

# Create app folder
mkdir frappe_fabric

# Copy all files from source folder
cp -r /path/to/frappe_fabric_app/* frappe_fabric/
```

### Step 2: Install App

```bash
# From frappe-bench directory
cd ~/frappe-bench

# Install dependencies
bench setup requirements

# Install app on site
bench --site your-site.local install-app frappe_fabric

# Run migrations
bench migrate

# Clear cache
bench clear-cache

# Build assets
bench build

# Restart server
bench restart
```

### Step 3: Verify Installation

```bash
# Check installed apps
bench --site your-site.local list-apps

# Should show: frappe_fabric
```

## File Structure

```
frappe_fabric_app/
├── frappe_fabric/
│   ├── __init__.py                 # Module initialization
│   ├── hooks.py                    # App settings
│   ├── install.py                  # Installation scripts
│   │
│   ├── api/                        # REST APIs
│   │   ├── __init__.py
│   │   ├── roll.py                 # Roll APIs
│   │   ├── receipt.py              # Receipt APIs
│   │   ├── cutting.py              # Cutting and Sales APIs
│   │   └── reports.py              # Reports APIs
│   │
│   ├── utils/                      # Helper tools
│   │   ├── __init__.py
│   │   ├── roll_utils.py           # Roll utilities
│   │   ├── qr_generator.py         # QR code generation
│   │   └── accounting_utils.py     # Accounting entries
│   │
│   └── fabric_management/          # Main module
│       └── doctype/                # DocTypes
│
├── setup.py                        # Setup file
├── requirements.txt                # Dependencies
└── README.md                       # Documentation
```

## Required DocTypes

The app includes all required DocTypes. They will be created automatically during installation.

### 1. Fabric Item

Main DocType for fabric items.

Key fields:
- item_code: Item code (Primary)
- item_name: Item name
- fabric_type: Fabric type
- width: Width in cm
- standard_rate: Selling price

### 2. Fabric Roll

Main DocType for individual rolls.

Key fields:
- roll_number: Roll number (Primary)
- item_code: Link to Fabric Item
- original_length: Original length
- current_length: Current length
- warehouse: Warehouse
- status: Status

## Integration with React Frontend

### Service File

```typescript
// src/services/fabric.service.ts

const ERPNEXT_URL = import.meta.env.VITE_ERPNEXT_URL;
const API_KEY = import.meta.env.VITE_ERPNEXT_API_KEY;
const API_SECRET = import.meta.env.VITE_ERPNEXT_API_SECRET;

const headers = {
  'Authorization': 'token ' + API_KEY + ':' + API_SECRET,
  'Content-Type': 'application/json'
};

export const fabricService = {
  async getRoll(rollNumber: string) {
    const response = await fetch(
      ERPNEXT_URL + '/api/method/frappe_fabric.api.roll.get_roll?roll_number=' + rollNumber,
      { headers }
    );
    return response.json();
  },

  async createContainerReceipt(data: any) {
    const response = await fetch(
      ERPNEXT_URL + '/api/method/frappe_fabric.api.receipt.create_container_receipt',
      {
        method: 'POST',
        headers,
        body: JSON.stringify({ data })
      }
    );
    return response.json();
  }
};
```

---

**Updated:** January 2024
**Version:** 1.0.0
