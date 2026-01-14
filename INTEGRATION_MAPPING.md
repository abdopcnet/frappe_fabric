# Integration Mapping

React frontend to Frappe API endpoints mapping.

## 1. Product Tree (EnhancedProductTree)

| Action | API Endpoint |
|--------|--------------|
| Show Items | frappe_fabric.api.roll.search_rolls |
| Roll Details | frappe_fabric.api.roll.get_roll |
| Roll Movements | frappe_fabric.api.roll.get_roll_movements |
| Update Location | frappe_fabric.api.roll.update_roll_location |

## 2. Material Receipt

| Action | API Endpoint |
|--------|--------------|
| Create Receipt | frappe_fabric.api.receipt.create_container_receipt |
| Scan Roll | frappe_fabric.api.receipt.scan_roll |
| Complete Receipt | frappe_fabric.api.receipt.complete_receipt |

## 3. Sample Cutting and Sales

| Action | API Endpoint |
|--------|--------------|
| Sample Cutting | frappe_fabric.api.cutting.create_sample_cutting |
| Retail Sale | frappe_fabric.api.cutting.create_retail_sale |

## 4. Reports

| Action | API Endpoint |
|--------|--------------|
| Stock Balance | frappe_fabric.api.reports.get_stock_balance |
| Movements | frappe_fabric.api.reports.get_movement_history |
| Sales | frappe_fabric.api.reports.get_sales_report |

## Environment Variables

```
VITE_ERPNEXT_URL=https://your-site.erpnext.com
VITE_ERPNEXT_API_KEY=your_api_key
VITE_ERPNEXT_API_SECRET=your_api_secret
```