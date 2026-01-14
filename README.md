# Frappe Fabric Management App
# تطبيق إدارة الأقمشة والرولونات

## 📋 نظرة عامة

تطبيق Frappe/ERPNext متكامل لإدارة مخزون الأقمشة مع تتبع الرولونات بشكل فردي باستخدام QR Codes.

## ✨ المميزات

- ✅ تتبع الرولونات بشكل فردي
- ✅ استلام الكونتينرات والشحنات
- ✅ قص العينات مع القيود المحاسبية
- ✅ البيع المفرد (قص وبيع)
- ✅ مناقلة بين المستودعات
- ✅ الجرد والتسويات
- ✅ طباعة لصاقات QR
- ✅ تقارير شاملة
- ✅ APIs جاهزة للربط

## 📦 المتطلبات

- Frappe Framework v14+
- ERPNext v14+
- Python 3.10+

## 🚀 التثبيت

[code]bash
# 1. الانتقال لمجلد التطبيقات
cd frappe-bench/apps

# 2. نسخ التطبيق
git clone https://github.com/your-repo/frappe_fabric.git

# 3. تثبيت التطبيق
bench --site your-site.local install-app frappe_fabric

# 4. تطبيق التغييرات
bench migrate

# 5. إعادة تشغيل الخادم
bench restart
[code]

## 📁 هيكل المشروع

[code]
frappe_fabric/
├── frappe_fabric/
│   ├── __init__.py
│   ├── hooks.py
│   ├── install.py
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
│           ├── container_receipt/
│           └── ...
├── setup.py
└── requirements.txt
[code]

## 📖 التوثيق

- [دليل التثبيت](INSTALLATION_GUIDE.md)
- [مرجع APIs](API_REFERENCE.md)
- [مخطط الجداول](DOCTYPES_SCHEMA.md)

## 🔗 الروابط

- [Frappe Documentation](https://frappeframework.com/docs)
- [ERPNext Documentation](https://docs.erpnext.com)

---

**الإصدار:** 1.0.0
**الترخيص:** MIT
