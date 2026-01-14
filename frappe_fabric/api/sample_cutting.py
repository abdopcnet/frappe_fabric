"""
Sample Cutting API
==================
API endpoints for Sample Cutting DocType
"""

import frappe
from frappe import _
import json


@frappe.whitelist()
def get(name):
    """Get a single Sample Cutting by name"""
    doc = frappe.get_doc("Sample Cutting", name)
    if not doc.has_permission("read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    return doc.as_dict()


@frappe.whitelist()
def get_list(filters=None, fields=None, limit_start=0, limit_page_length=20, order_by=None):
    """Get list of Sample Cuttings"""
    if isinstance(filters, str):
        filters = json.loads(filters)
    
    return frappe.get_list(
        "Sample Cutting",
        filters=filters or {},
        fields=fields or "*",
        limit_start=limit_start,
        limit_page_length=limit_page_length,
        order_by=order_by
    )


@frappe.whitelist()
def create(data):
    """Create a new Sample Cutting"""
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc({
        "doctype": "Sample Cutting",
        **data
    })
    doc.insert()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def update(name, data):
    """Update a Sample Cutting"""
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc("Sample Cutting", name)
    if not doc.has_permission("write"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.update(data)
    doc.save()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def delete(name):
    """Delete a Sample Cutting"""
    doc = frappe.get_doc("Sample Cutting", name)
    if not doc.has_permission("delete"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.delete()
    frappe.db.commit()
    return {"message": _("Sample Cutting deleted successfully")}


@frappe.whitelist()
def submit(name):
    """Submit a Sample Cutting"""
    doc = frappe.get_doc("Sample Cutting", name)
    if not doc.has_permission("submit"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.submit()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def cancel(name):
    """Cancel a Sample Cutting"""
    doc = frappe.get_doc("Sample Cutting", name)
    if not doc.has_permission("cancel"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.cancel()
    frappe.db.commit()
    return doc.as_dict()
