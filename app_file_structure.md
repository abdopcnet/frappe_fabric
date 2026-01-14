# App File Structure

Complete file structure of the Frappe Fabric Management application.

## Directory Tree

```
frappe_fabric/
├── frappe_fabric/
│   ├── __init__.py
│   ├── hooks.py
│   ├── install.py
│   ├── modules.txt
│   ├── public/
│   │   ├── .gitkeep
│   │   ├── css/
│   │   └── js/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── roll.py
│   │   ├── receipt.py
│   │   ├── cutting.py
│   │   └── reports.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── roll_utils.py
│   │   ├── qr_generator.py
│   │   └── accounting_utils.py
│   └── fabric_management/
│       ├── __init__.py
│       └── doctype/
│           ├── __init__.py
│           ├── fabric_item/
│           ├── fabric_color/
│           ├── fabric_batch/
│           ├── fabric_roll/
│           ├── container_receipt/
│           ├── container_receipt_expected_item/
│           ├── container_receipt_roll/
│           ├── sample_cutting/
│           ├── sample_cutting_item/
│           ├── retail_cutting_sale/
│           ├── roll_transfer/
│           ├── roll_transfer_item/
│           └── roll_movement/
├── pyproject.toml
├── requirements.txt
└── README.md
```

## File Descriptions

### Root Level Files

- **pyproject.toml**: Python package configuration
- **requirements.txt**: Python dependencies
- **README.md**: Main application documentation

### Core Application Files

#### `frappe_fabric/`
- **__init__.py**: Package initialization with version
- **hooks.py**: App configuration and hooks
- **install.py**: Installation hooks and setup functions
- **modules.txt**: Module definitions

### API Module (`frappe_fabric/api/`)

- **roll.py**: Roll management APIs (get, search, update, reserve)
- **receipt.py**: Container receipt APIs (create, get, scan)
- **cutting.py**: Cutting and sales APIs (sample cutting, retail sales)
- **reports.py**: Reporting APIs (stock balance, movements, cutting summary)

### Utilities Module (`frappe_fabric/utils/`)

- **roll_utils.py**: Roll utility functions
- **qr_generator.py**: QR code generation utilities
- **accounting_utils.py**: Accounting entry creation functions

### DocTypes (`frappe_fabric/fabric_management/doctype/`)

Each DocType directory contains:
- **__init__.py**: Package initialization
- **{doctype}.py**: Python controller class
- **{doctype}.json**: DocType definition (fields, permissions, etc.)
- **{doctype}.js**: Client-side JavaScript (form scripts)

#### Main DocTypes

1. **fabric_item**: Fabric item master data
2. **fabric_color**: Color master data
3. **fabric_batch**: Batch master data
4. **fabric_roll**: Individual roll tracking (main entity)
5. **roll_movement**: Movement history log

#### Transaction DocTypes

6. **container_receipt**: Container/shipment receipt (submittable)
7. **sample_cutting**: Sample cutting transactions (submittable)
8. **retail_cutting_sale**: Retail cutting sales (submittable)
9. **roll_transfer**: Roll transfers between warehouses (submittable)

#### Child Tables

- **container_receipt_expected_item**: Expected items in container receipt
- **container_receipt_roll**: Received rolls in container receipt
- **sample_cutting_item**: Items in sample cutting
- **roll_transfer_item**: Items in roll transfer

## Statistics

- **Total Python Files**: 39
- **Total DocTypes**: 13
- **API Files**: 4
- **Utility Files**: 3
