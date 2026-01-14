# Custom Fields Usage

Documentation of custom fields used by the Frappe Fabric Management application.

## Custom Fields Created by App

### Item DocType

The app creates custom fields on the standard **Item** DocType to mark fabric items.

#### Field: `is_fabric_item`

| Property | Value |
|----------|-------|
| **DocType** | Item |
| **Fieldname** | is_fabric_item |
| **Label** | Is Fabric Item |
| **Fieldtype** | Check |
| **Insert After** | item_group |
| **Description** | Checkbox to mark if an item is a fabric item |

**Usage:**
- Used to identify fabric items in the standard Item master
- Can be used in filters to show only fabric items
- Linked to Fabric Item master records

**Created By:**
- Function: `frappe_fabric.install.create_custom_fields()`
- Called during: App installation (`after_install` hook)

## Custom Fields in App DocTypes

The app uses standard fields in its own DocTypes. All custom fields are defined in the DocType JSON files.

### Fabric Item DocType

No external custom fields - all fields are part of the DocType definition.

### Fabric Roll DocType

No external custom fields - all fields are part of the DocType definition.

### Container Receipt DocType

No external custom fields - all fields are part of the DocType definition.

## Integration with Standard DocTypes

### Item Integration

- **Custom Field**: `is_fabric_item` (Checkbox)
- **Purpose**: Link standard Item records with Fabric Item records
- **Usage**: Filter and identify fabric items in Item list

### Warehouse Integration

- **Usage**: Standard Warehouse DocType is used directly
- **No Custom Fields**: App uses standard warehouse fields

### Supplier Integration

- **Usage**: Standard Supplier DocType is used directly
- **No Custom Fields**: App uses standard supplier fields

### Customer Integration

- **Usage**: Standard Customer DocType is used directly (for retail sales)
- **No Custom Fields**: App uses standard customer fields

## Field Dependencies

### Custom Field Dependencies

- `Item.is_fabric_item` → Used to link with `Fabric Item` records

### Standard Field Usage

The app uses these standard DocType fields:

- **Item**: item_code, item_name, item_group
- **Warehouse**: name (warehouse code)
- **Supplier**: name (supplier code)
- **Customer**: name (customer code)

## Installation

Custom fields are automatically created during app installation via the `after_install` hook in `frappe_fabric/install.py`.

### Manual Creation

If you need to recreate custom fields manually:

```python
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

create_custom_field("Item", {
    "fieldname": "is_fabric_item",
    "label": "Is Fabric Item",
    "fieldtype": "Check",
    "insert_after": "item_group"
})
```

## Fixtures

Custom fields can be exported as fixtures and imported to other sites:

```python
# In hooks.py
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["module", "=", "Frappe Fabric"]]
    }
]
```

## Notes

- All custom fields are created in the `Frappe Fabric` module
- Custom fields are version-controlled through the app's fixture system
- Standard DocTypes (Item, Warehouse, etc.) are not modified beyond custom fields
- The app follows Frappe best practices for custom field management
