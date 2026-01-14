"""
Roll Transfer API
=================
API endpoints for Roll Transfer DocType
"""

import frappe
from frappe import _
import json


@frappe.whitelist()
def get(name):
    """Get a single Roll Transfer by name"""
    doc = frappe.get_doc("Roll Transfer", name)
    if not doc.has_permission("read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    return doc.as_dict()


@frappe.whitelist()
def get_list(filters=None, fields=None, limit_start=0, limit_page_length=20, order_by=None):
    """Get list of Roll Transfers"""
    if isinstance(filters, str):
        filters = json.loads(filters)
    
    return frappe.get_list(
        "Roll Transfer",
        filters=filters or {},
        fields=fields or "*",
        limit_start=limit_start,
        limit_page_length=limit_page_length,
        order_by=order_by
    )


@frappe.whitelist()
def create(data):
    """Create a new Roll Transfer"""
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc({
        "doctype": "Roll Transfer",
        **data
    })
    doc.insert()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def update(name, data):
    """Update a Roll Transfer"""
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc("Roll Transfer", name)
    if not doc.has_permission("write"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.update(data)
    doc.save()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def delete(name):
    """Delete a Roll Transfer"""
    doc = frappe.get_doc("Roll Transfer", name)
    if not doc.has_permission("delete"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.delete()
    frappe.db.commit()
    return {"message": _("Roll Transfer deleted successfully")}


@frappe.whitelist()
def submit(name):
    """Submit a Roll Transfer"""
    doc = frappe.get_doc("Roll Transfer", name)
    if not doc.has_permission("submit"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.submit()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def cancel(name):
    """Cancel a Roll Transfer"""
    doc = frappe.get_doc("Roll Transfer", name)
    if not doc.has_permission("cancel"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.cancel()
    frappe.db.commit()
    return doc.as_dict()
