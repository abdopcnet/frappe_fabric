# DocTypes Schema - مخطط الجداول
# Frappe Fabric Management DocTypes

---

## 📋 قائمة DocTypes

| # | DocType | النوع | الوصف |
|---|---------|------|-------|
| 1 | Fabric Item | Main | تعريف أنواع الأقمشة |
| 2 | Fabric Color | Main | ألوان الأقمشة |
| 3 | Fabric Batch | Main | دفعات الاستيراد |
| 4 | Fabric Roll | Main | الرولونات الفردية |
| 5 | Roll Movement | Main | سجل الحركات |
| 6 | Container Receipt | Submittable | استلام الكونتينرات |
| 7 | Container Receipt Expected Item | Child | البنود المتوقعة |
| 8 | Container Receipt Roll | Child | الرولونات المستلمة |
| 9 | Sample Cutting | Submittable | قص العينات |
| 10 | Sample Cutting Item | Child | بنود القص |
| 11 | Retail Cutting Sale | Submittable | البيع المفرد |
| 12 | Roll Transfer | Submittable | مناقلة الرولونات |
| 13 | Roll Transfer Item | Child | بنود المناقلة |

---

## 1️⃣ Fabric Item (المادة)

**الإعدادات:**
- Module: Fabric Management
- Is Submittable: No
- Quick Entry: Yes

**الحقول:**

| # | Fieldname | Label | Type | Required |
|---|-----------|-------|------|----------|
| 1 | item_code | كود المادة | Data | ✅ |
| 2 | item_name | اسم المادة | Data | ✅ |
| 3 | fabric_type | نوع القماش | Select | |
| 4 | width | العرض (سم) | Float | |
| 5 | standard_rate | سعر البيع/متر | Currency | |
| 6 | valuation_rate | سعر التكلفة/متر | Currency | |

---

## 4️⃣ Fabric Roll (الرولون) ⭐

**الإعدادات:**
- Module: Fabric Management
- Autoname: ROLL-.YYYY.-.#####

**الحقول:**

| # | Fieldname | Label | Type | Required |
|---|-----------|-------|------|----------|
| 1 | roll_number | رقم الرولون | Data | ✅ |
| 2 | item_code | كود المادة | Link: Fabric Item | ✅ |
| 3 | original_length | الطول الأصلي (م) | Float | ✅ |
| 4 | current_length | الطول الحالي (م) | Float | ✅ |
| 5 | warehouse | المستودع | Link: Warehouse | ✅ |
| 6 | status | الحالة | Select | |
| 7 | qr_code | QR Code | Attach Image | |

---

## 6️⃣ Container Receipt (استلام الكونتينر)

**الإعدادات:**
- Module: Fabric Management
- Is Submittable: Yes
- Autoname: CR-.YYYY.-.#####

**الحقول:**

| # | Fieldname | Label | Type | Required |
|---|-----------|-------|------|----------|
| 1 | container_number | رقم الكونتينر | Data | ✅ |
| 2 | posting_date | تاريخ الاستلام | Date | ✅ |
| 3 | supplier | المورد | Link: Supplier | |
| 4 | warehouse | المستودع | Link: Warehouse | ✅ |
| 5 | expected_items | البنود المتوقعة | Table | |
| 6 | received_rolls | الرولونات المستلمة | Table | |
| 7 | status | الحالة | Select | |

---

## 📝 ملاحظات للمبرمج

### ترتيب الإنشاء:
1. Fabric Color
2. Fabric Item
3. Fabric Batch
4. Fabric Roll
5. Roll Movement
6. Child Tables
7. Main Documents

### الصلاحيات:
| DocType | Fabric Manager | Fabric User | Fabric Viewer |
|---------|---------------|-------------|---------------|
| Fabric Item | Full | Read, Write | Read |
| Fabric Roll | Full | Read, Write | Read |
| Container Receipt | Full | Read, Write, Create | Read |

---

**تاريخ التحديث:** يناير 2024
**الإصدار:** 1.0.0
