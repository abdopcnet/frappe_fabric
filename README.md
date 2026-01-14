# Frappe Fabric Management App

## Overview

Frappe Fabric Management is a complete ERPNext application for managing fabric inventory with individual roll tracking using QR codes. It provides full lifecycle management from container receipt to retail sales.

## Features

### Core Features

- **Individual Roll Tracking**: Track each fabric roll with unique QR codes
- **Container Receipt Management**: Receive containers and shipments with expected vs actual tracking
- **Sample Cutting**: Cut samples with accounting entries
- **Retail Cutting Sales**: Single-piece cutting and sales (cut and sell)
- **Warehouse Transfers**: Transfer rolls between warehouses
- **Stock Take & Adjustments**: Inventory adjustments and stocktaking
- **QR Code Printing**: Generate and print QR code labels
- **Comprehensive Reports**: Stock balance, movement history, and sales reports
- **REST APIs**: Complete API suite for integration

### Key Capabilities

- Real-time stock tracking with available/reserved quantities
- Automatic movement history tracking
- Cost tracking per meter
- Multi-warehouse support
- Batch tracking
- Color management
- Accounting integration

## Requirements

- Frappe Framework v15+
- ERPNext v15+
- Python 3.10+

## Installation

```bash
# 1. Navigate to apps directory
cd frappe-bench/apps

# 2. Get the app
bench get-app frappe_fabric

# 3. Install on site
bench --site your-site.local install-app frappe_fabric

# 4. Run migrations
bench --site your-site.local migrate

# 5. Restart services
bench restart
```

## Project Structure

```
frappe_fabric/
├── frappe_fabric/
│   ├── __init__.py
│   ├── hooks.py
│   ├── install.py
│   ├── modules.txt
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
│           ├── fabric_roll/
│           ├── fabric_color/
│           ├── fabric_batch/
│           ├── container_receipt/
│           ├── sample_cutting/
│           ├── retail_cutting_sale/
│           ├── roll_transfer/
│           └── roll_movement/
├── pyproject.toml
└── requirements.txt
```

## Documentation

- [Installation Guide](INSTALLATION_GUIDE.md)
- [API Reference](API_REFERENCE.md)
- [DocType Schema](DOCTYPES_SCHEMA.md)
- [Integration Mapping](INTEGRATION_MAPPING.md)
- [App File Structure](app_file_structure.md)
- [API Tree](app_api_tree.md)
- [Workflow Diagrams](app_workflow.md)
- [Custom Fields Usage](app_used_custom_fields.md)

## API Documentation

Detailed API documentation is available in the `docs/api/` directory:

- [Roll APIs](docs/api/roll.md)
- [Receipt APIs](docs/api/receipt.md)
- [Cutting APIs](docs/api/cutting.md)
- [Reports APIs](docs/api/reports.md)

## License

MIT

## Version

1.0.0
