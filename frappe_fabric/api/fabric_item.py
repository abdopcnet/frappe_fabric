"""
Fabric Item API
===============
API endpoints for Fabric Item DocType
"""

import frappe
from frappe import _
import json


@frappe.whitelist()
def get(name):
    """
    Get a single Fabric Item by name
    
    Args:
        name: Document name
        
    Returns:
        dict: Fabric Item document
    """
    doc = frappe.get_doc("Fabric Item", name)
    if not doc.has_permission("read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    return doc.as_dict()


@frappe.whitelist()
def get_list(filters=None, fields=None, limit_start=0, limit_page_length=20, order_by=None):
    """
    Get list of Fabric Items
    
    Args:
        filters: JSON string or dict of filters
        fields: List of fields to fetch
        limit_start: Start at this index
        limit_page_length: Number of items to fetch
        order_by: Order by field
        
    Returns:
        list: List of Fabric Item documents
    """
    if isinstance(filters, str):
        filters = json.loads(filters)
    
    return frappe.get_list(
        "Fabric Item",
        filters=filters or {},
        fields=fields or "*",
        limit_start=limit_start,
        limit_page_length=limit_page_length,
        order_by=order_by
    )


@frappe.whitelist()
def create(data):
    """
    Create a new Fabric Item
    
    Args:
        data: JSON string or dict with document data
        
    Returns:
        dict: Created Fabric Item document
    """
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc({
        "doctype": "Fabric Item",
        **data
    })
    doc.insert()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def update(name, data):
    """
    Update a Fabric Item
    
    Args:
        name: Document name
        data: JSON string or dict with fields to update
        
    Returns:
        dict: Updated Fabric Item document
    """
    if isinstance(data, str):
        data = json.loads(data)
    
    doc = frappe.get_doc("Fabric Item", name)
    if not doc.has_permission("write"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.update(data)
    doc.save()
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist()
def delete(name):
    """
    Delete a Fabric Item
    
    Args:
        name: Document name
        
    Returns:
        dict: Success message
    """
    doc = frappe.get_doc("Fabric Item", name)
    if not doc.has_permission("delete"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    doc.delete()
    frappe.db.commit()
    return {"message": _("Fabric Item deleted successfully")}
