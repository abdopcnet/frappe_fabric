# DocTypes Schema

Frappe Fabric Management DocTypes structure.

## DocTypes List

| # | DocType | Type | Description |
|---|---------|------|-------------|
| 1 | Fabric Item | Main | Fabric item definitions |
| 2 | Fabric Color | Main | Fabric colors |
| 3 | Fabric Batch | Main | Import batches |
| 4 | Fabric Roll | Main | Individual rolls |
| 5 | Roll Movement | Main | Movement log |
| 6 | Container Receipt | Submittable | Container receipts |
| 7 | Container Receipt Expected Item | Child | Expected items |
| 8 | Container Receipt Roll | Child | Received rolls |
| 9 | Sample Cutting | Submittable | Sample cutting |
| 10 | Sample Cutting Item | Child | Cutting items |
| 11 | Retail Cutting Sale | Submittable | Retail sales |
| 12 | Roll Transfer | Submittable | Roll transfers |
| 13 | Roll Transfer Item | Child | Transfer items |

## 1. Fabric Item

**Settings:**
- Module: Fabric Management
- Is Submittable: No
- Quick Entry: Yes

**Key Fields:**

| Fieldname | Label | Type | Required |
|-----------|-------|------|----------|
| item_code | Item Code | Data | Yes |
| item_name | Item Name | Data | Yes |
| fabric_type | Fabric Type | Select | No |
| width | Width (cm) | Float | No |
| standard_rate | Selling Price/Meter | Currency | No |
| valuation_rate | Cost Price/Meter | Currency | No |

## 4. Fabric Roll

**Settings:**
- Module: Fabric Management
- Autoname: ROLL-.YYYY.-.#####

**Key Fields:**

| Fieldname | Label | Type | Required |
|-----------|-------|------|----------|
| roll_number | Roll Number | Data | Yes |
| item_code | Item Code | Link: Fabric Item | Yes |
| original_length | Original Length (m) | Float | Yes |
| current_length | Current Length (m) | Float | Yes |
| warehouse | Warehouse | Link: Warehouse | Yes |
| status | Status | Select | No |
| qr_code | QR Code | Attach Image | No |

## 6. Container Receipt

**Settings:**
- Module: Fabric Management
- Is Submittable: Yes
- Autoname: CR-.YYYY.-.#####

**Key Fields:**

| Fieldname | Label | Type | Required |
|-----------|-------|------|----------|
| container_number | Container Number | Data | Yes |
| posting_date | Receipt Date | Date | Yes |
| supplier | Supplier | Link: Supplier | No |
| warehouse | Warehouse | Link: Warehouse | Yes |
| expected_items | Expected Items | Table | No |
| received_rolls | Received Rolls | Table | No |
| status | Status | Select | No |

## Creation Order

1. Fabric Color
2. Fabric Item
3. Fabric Batch
4. Fabric Roll
5. Roll Movement
6. Child Tables
7. Main Documents

## Permissions

| DocType | Fabric Manager | Fabric User | Fabric Viewer |
|---------|---------------|-------------|---------------|
| Fabric Item | Full | Read, Write | Read |
| Fabric Roll | Full | Read, Write | Read |
| Container Receipt | Full | Read, Write, Create | Read |

---

**Updated:** January 2024
**Version:** 1.0.0
