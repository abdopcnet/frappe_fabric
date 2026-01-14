import frappe
from frappe import _

def after_install():
    """Setup after app installation"""
    create_roles()
    create_custom_fields()
    create_default_settings()
    frappe.db.commit()

def create_roles():
    """Create fabric management roles"""
    roles = [
        {"role_name": "Fabric Manager", "desk_access": 1},
        {"role_name": "Fabric User", "desk_access": 1},
        {"role_name": "Fabric Viewer", "desk_access": 1}
    ]
    
    for role in roles:
        if not frappe.db.exists("Role", role["role_name"]):
            doc = frappe.new_doc("Role")
            doc.role_name = role["role_name"]
            doc.desk_access = role["desk_access"]
            doc.insert()

def create_custom_fields():
    """Create custom fields in standard doctypes"""
    custom_fields = {
        "Item": [
            {
                "fieldname": "is_fabric_item",
                "label": "Is Fabric Item",
                "fieldtype": "Check",
                "insert_after": "item_group"
            }
        ]
    }
    
    for doctype, fields in custom_fields.items():
        for field in fields:
            if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": field["fieldname"]}):
                doc = frappe.new_doc("Custom Field")
                doc.dt = doctype
                doc.update(field)
                doc.insert()

def create_default_settings():
    """Create default fabric settings"""
    pass
