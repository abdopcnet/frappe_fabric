# API Reference - مرجع واجهات البرمجة
# Frappe Fabric Management APIs

---

## 🔐 المصادقة (Authentication)

جميع الطلبات تتطلب مصادقة عبر API Key:

[code]
Authorization: token {API_KEY}:{API_SECRET}
Content-Type: application/json
[code]

---

## 📦 Roll APIs - واجهات الرولونات

### GET /api/method/frappe_fabric.api.roll.get_roll
جلب بيانات رولون محدد

**المعاملات:**
| المعامل | النوع | مطلوب | الوصف |
|---------|------|-------|-------|
| roll_number | string | ✅ | رقم الرولون |

**الاستجابة:**
[code]json
{
  "message": {
    "roll_number": "ROLL-20240115-0001-ABCD",
    "item_code": "FAB-001",
    "item_name": "قماش قطني أبيض",
    "current_length": 45.0,
    "warehouse": "Main Warehouse",
    "status": "Available"
  }
}
[code]

---

### POST /api/method/frappe_fabric.api.roll.search_rolls
البحث في الرولونات

**الجسم (Body):**
[code]json
{
  "filters": {
    "item_code": "FAB-001",
    "warehouse": "Main Warehouse",
    "status": "Available",
    "min_length": 10
  },
  "page": 1,
  "page_size": 20
}
[code]

---

## 📥 Receipt APIs - واجهات الاستلام

### POST /api/method/frappe_fabric.api.receipt.create_container_receipt
إنشاء استلام كونتينر جديد

**الجسم:**
[code]json
{
  "data": {
    "container_number": "CONT-1001",
    "supplier": "SUP-001",
    "warehouse": "Main Warehouse",
    "expected_items": [
      {
        "item_code": "FAB-001",
        "expected_rolls": 100,
        "expected_meters": 5000
      }
    ]
  }
}
[code]

---

### POST /api/method/frappe_fabric.api.receipt.scan_roll
مسح/إضافة رولون للاستلام

**الجسم:**
[code]json
{
  "receipt_no": "CR-2024-0001",
  "roll_data": {
    "item_code": "FAB-001",
    "color": "White",
    "scanned_length": 50.5,
    "bin_location": "A-01-02"
  }
}
[code]

---

## ✂️ Cutting APIs - واجهات القص والبيع

### POST /api/method/frappe_fabric.api.cutting.create_sample_cutting
إنشاء قص عينات

**الجسم:**
[code]json
{
  "data": {
    "warehouse": "Main Warehouse",
    "purpose": "Customer Sample",
    "expense_account": "Sample Cutting Expenses - TC",
    "items": [
      {
        "roll_number": "ROLL-20240115-0001-ABCD",
        "cut_qty": 2.5
      }
    ],
    "submit": true
  }
}
[code]

---

### POST /api/method/frappe_fabric.api.cutting.create_retail_sale
إنشاء بيع مفرد

**الجسم:**
[code]json
{
  "data": {
    "roll_number": "ROLL-20240115-0001-ABCD",
    "cut_qty": 5.0,
    "rate": 25.00,
    "sale_type": "Cash",
    "submit": true
  }
}
[code]

---

## 📊 Reports APIs - واجهات التقارير

### POST /api/method/frappe_fabric.api.reports.get_stock_balance
تقرير رصيد المخزون

**الجسم:**
[code]json
{
  "filters": {
    "item_code": "FAB-001",
    "warehouse": "Main Warehouse"
  }
}
[code]

---

**تاريخ التحديث:** يناير 2024
**الإصدار:** 1.0.0
