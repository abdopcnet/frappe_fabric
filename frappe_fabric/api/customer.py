"""
Customer API
============
API endpoints for Customer DocType
"""

import frappe
from frappe import _
import json


@frappe.whitelist()
def get(name):
    """Get a single Customer by name"""
    doc = frappe.get_doc("Customer", name)
    if not doc.has_permission("read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    return doc.as_dict()


@frappe.whitelist()
def get_list(filters=None, fields=None, limit_start=0, limit_page_length=20, order_by=None):
    """Get list of Customers"""
    if isinstance(filters, str):
        filters = json.loads(filters)
    
    return frappe.get_list(
        "Customer",
        filters=filters or {},
        fields=fields or "*",
        limit_start=limit_start,
        limit_page_length=limit_page_length,
        order_by=order_by
    )


@frappe.whitelist()
def create(data):
    """Create a new Customer"""
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc({
        "doctype": "Customer",
        **data
    })
    doc.insert()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def update(name, data):
    """Update a Customer"""
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc("Customer", name)
    if not doc.has_permission("write"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.update(data)
    doc.save()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def delete(name):
    """Delete a Customer"""
    doc = frappe.get_doc("Customer", name)
    if not doc.has_permission("delete"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.delete()
    frappe.db.commit()
    return {"message": _("Customer deleted successfully")}
