# دليل التثبيت والتشغيل الكامل
# Frappe Fabric Management App Installation Guide

---

## 📋 المتطلبات الأساسية

### البرمجيات المطلوبة:
- Frappe Framework v14 أو أحدث
- ERPNext v14 أو أحدث
- Python 3.10+
- Node.js 18+
- MariaDB 10.6+
- Redis

### المكتبات الإضافية:
[code]bash
pip install qrcode Pillow
[code]

---

## 🚀 خطوات التثبيت

### الخطوة 1: نسخ الملفات

[code]bash
# الانتقال لمجلد التطبيقات
cd ~/frappe-bench/apps

# إنشاء مجلد التطبيق
mkdir frappe_fabric

# نسخ جميع الملفات من المجلد المرفق
cp -r /path/to/frappe_fabric_app/* frappe_fabric/
[code]

### الخطوة 2: تثبيت التطبيق

[code]bash
# من مجلد frappe-bench
cd ~/frappe-bench

# تثبيت التبعيات
bench setup requirements

# تثبيت التطبيق على الموقع
bench --site your-site.local install-app frappe_fabric

# تطبيق التغييرات
bench migrate

# مسح الكاش
bench clear-cache

# إعادة بناء الأصول
bench build

# إعادة تشغيل الخادم
bench restart
[code]

### الخطوة 3: التحقق من التثبيت

[code]bash
# التحقق من التطبيقات المثبتة
bench --site your-site.local list-apps

# يجب أن يظهر: frappe_fabric
[code]

---

## 📁 هيكل الملفات

[code]
frappe_fabric_app/
├── frappe_fabric/
│   ├── __init__.py                 # تهيئة الموديول
│   ├── hooks.py                    # إعدادات التطبيق
│   ├── install.py                  # سكربتات التثبيت
│   │
│   ├── api/                        # REST APIs
│   │   ├── __init__.py
│   │   ├── roll.py                 # APIs الرولونات
│   │   ├── receipt.py              # APIs الاستلام
│   │   ├── cutting.py              # APIs القص والبيع
│   │   └── reports.py              # APIs التقارير
│   │
│   ├── utils/                      # أدوات مساعدة
│   │   ├── __init__.py
│   │   ├── roll_utils.py           # أدوات الرولون
│   │   ├── qr_generator.py         # توليد QR
│   │   └── accounting_utils.py     # القيود المحاسبية
│   │
│   └── fabric_management/          # الموديول الرئيسي
│       └── doctype/                # DocTypes
│
├── setup.py                        # ملف الإعداد
├── requirements.txt                # التبعيات
└── README.md                       # التوثيق
[code]

---

## 🗂️ DocTypes المطلوب إنشاؤها

### 1. Fabric Item (المادة)
| الحقل | النوع | الوصف |
|-------|------|-------|
| item_code | Data | كود المادة (Primary) |
| item_name | Data | اسم المادة |
| fabric_type | Select | نوع القماش |
| width | Float | العرض بالسم |
| standard_rate | Currency | سعر البيع |

### 2. Fabric Roll (الرولون)
| الحقل | النوع | الوصف |
|-------|------|-------|
| roll_number | Data | رقم الرولون (Primary) |
| item_code | Link: Fabric Item | كود المادة |
| original_length | Float | الطول الأصلي |
| current_length | Float | الطول الحالي |
| warehouse | Link: Warehouse | المستودع |
| status | Select | الحالة |

---

## 📊 الربط مع واجهات React

### ملف خدمة الاتصال

[code]typescript
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
[code]

---

**تاريخ التحديث:** يناير 2024
**الإصدار:** 1.0.0
