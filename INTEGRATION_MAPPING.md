# خريطة الربط بين واجهات React و APIs الفرابي

## 1. شجرة المنتجات (EnhancedProductTree)

| الإجراء | API Endpoint |
|---------|--------------|
| عرض المواد | frappe_fabric.api.roll.search_rolls |
| تفاصيل الرولون | frappe_fabric.api.roll.get_roll |
| حركات الرولون | frappe_fabric.api.roll.get_roll_movements |
| تحديث الموقع | frappe_fabric.api.roll.update_roll_location |

## 2. استلام المواد

| الإجراء | API Endpoint |
|---------|--------------|
| إنشاء استلام | frappe_fabric.api.receipt.create_container_receipt |
| مسح رولون | frappe_fabric.api.receipt.scan_roll |
| إكمال الاستلام | frappe_fabric.api.receipt.complete_receipt |

## 3. قص العينات والبيع

| الإجراء | API Endpoint |
|---------|--------------|
| قص عينات | frappe_fabric.api.cutting.create_sample_cutting |
| بيع مفرد | frappe_fabric.api.cutting.create_retail_sale |

## 4. التقارير

| الإجراء | API Endpoint |
|---------|--------------|
| رصيد المخزون | frappe_fabric.api.reports.get_stock_balance |
| حركات | frappe_fabric.api.reports.get_movement_history |
| المبيعات | frappe_fabric.api.reports.get_sales_report |

## إعداد متغيرات البيئة

VITE_ERPNEXT_URL=https://your-site.erpnext.com
VITE_ERPNEXT_API_KEY=your_api_key
VITE_ERPNEXT_API_SECRET=your_api_secret
