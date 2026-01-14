# API Tree

Complete API documentation reference for Frappe Fabric Management application.

## Custom APIs

Custom API endpoints for fabric management operations.

- [Roll APIs](docs/api/roll.md) - Roll management and tracking
- [Receipt APIs](docs/api/receipt.md) - Container receipt management
- [Cutting APIs](docs/api/cutting.md) - Sample cutting and retail sales
- [Reports APIs](docs/api/reports.md) - Reporting and analytics

## DocType APIs

Standard REST API endpoints for DocTypes.

### App DocTypes

- [Fabric Item API](docs/api/fabric_item.md)
- [Fabric Color API](docs/api/fabric_color.md)
- [Fabric Batch API](docs/api/fabric_batch.md)
- [Fabric Roll API](docs/api/fabric_roll.md)
- [Container Receipt API](docs/api/container_receipt.md)
- [Sample Cutting API](docs/api/sample_cutting.md)
- [Retail Cutting Sale API](docs/api/retail_cutting_sale.md)
- [Roll Transfer API](docs/api/roll_transfer.md)
- [Roll Movement API](docs/api/roll_movement.md)

### ERPNext DocTypes

- [Item API](docs/api/item.md)
- [Warehouse API](docs/api/warehouse.md)
- [Supplier API](docs/api/supplier.md)
- [Customer API](docs/api/customer.md)
- [Purchase Receipt API](docs/api/purchase_receipt.md)
- [Sales Invoice API](docs/api/sales_invoice.md)
- [Account API](docs/api/account.md)
- [Cost Center API](docs/api/cost_center.md)
- [Item Group API](docs/api/item_group.md)

## Authentication

All APIs require authentication via API Key:

```
Authorization: token {API_KEY}:{API_SECRET}
Content-Type: application/json
```
