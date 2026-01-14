# App File Structure

File structure of the Frappe Fabric Management application.

## Directory Structure

```
frappe_fabric/
├── frappe_fabric/
│   ├── __init__.py
│   ├── hooks.py
│   ├── install.py
│   ├── modules.txt
│   ├── public/
│   ├── api/
│   │   ├── roll.py
│   │   ├── receipt.py
│   │   ├── cutting.py
│   │   └── reports.py
│   ├── utils/
│   │   ├── roll_utils.py
│   │   ├── qr_generator.py
│   │   └── accounting_utils.py
│   └── fabric_management/
│       └── doctype/
│           ├── fabric_item/
│           ├── fabric_color/
│           ├── fabric_batch/
│           ├── fabric_roll/
│           ├── container_receipt/
│           ├── sample_cutting/
│           ├── retail_cutting_sale/
│           ├── roll_transfer/
│           └── roll_movement/
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Core Files

- **hooks.py** - App configuration and hooks
- **install.py** - Installation scripts
- **modules.txt** - Module definitions

## API Module

Custom API endpoints:

- **roll.py** - Roll management APIs
- **receipt.py** - Container receipt APIs
- **cutting.py** - Cutting and sales APIs
- **reports.py** - Reporting APIs

## Utilities Module

Helper functions:

- **roll_utils.py** - Roll utility functions
- **qr_generator.py** - QR code generation
- **accounting_utils.py** - Accounting functions

## DocTypes

Main DocTypes:

- **fabric_item** - Fabric item master data
- **fabric_color** - Color master data
- **fabric_batch** - Batch master data
- **fabric_roll** - Individual roll tracking
- **roll_movement** - Movement history log

Transaction DocTypes:

- **container_receipt** - Container receipts
- **sample_cutting** - Sample cutting transactions
- **retail_cutting_sale** - Retail sales
- **roll_transfer** - Roll transfers

Each DocType directory contains:

- `{doctype}.py` - Python controller
- `{doctype}.json` - DocType definition
- `{doctype}.js` - Client-side scripts
