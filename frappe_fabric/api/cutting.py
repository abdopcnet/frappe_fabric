"""
Cutting & Sales APIs
====================
APIs for sample cutting and retail cutting sales
"""

import frappe
from frappe import _
from frappe.utils import nowdate, nowtime, flt, cint
import json


@frappe.whitelist()
def create_sample_cutting(data):
    """
    Create a sample cutting document
    
    Args:
        data: dict with cutting details
            - warehouse: Source warehouse
            - purpose: Purpose of cutting
            - customer: Customer if applicable
            - expense_account: Account to charge
            - items: List of rolls to cut from
    
    Returns:
        dict: Created cutting info
    """
    if isinstance(data, str):
        data = json.loads(data)
    
    if not data.get("items"):
        frappe.throw(_("At least one item is required"))
    
    doc = frappe.new_doc("Sample Cutting")
    doc.posting_date = data.get("posting_date") or nowdate()
    doc.posting_time = data.get("posting_time") or nowtime()
    doc.warehouse = data.get("warehouse")
    doc.purpose = data.get("purpose", "Customer Sample")
    doc.customer = data.get("customer")
    doc.expense_account = data.get("expense_account")
    doc.cost_center = data.get("cost_center")
    doc.remarks = data.get("remarks")
    
    for item in data.get("items", []):
        roll_number = item.get("roll_number")
        cut_qty = flt(item.get("cut_qty"))
        
        if not roll_number:
            frappe.throw(_("Roll number is required for each item"))
        
        if cut_qty <= 0:
            frappe.throw(_("Cut quantity must be positive"))
        
        roll = frappe.get_doc("Fabric Roll", roll_number)
        
        if cut_qty > roll.available_length:
            frappe.throw(
                _("Cannot cut {0}m from roll {1}. Available: {2}m").format(
                    cut_qty, roll_number, roll.available_length
                )
            )
        
        doc.append("items", {
            "roll_number": roll_number,
            "item_code": roll.item_code,
            "item_name": roll.item_name,
            "color": roll.color,
            "balance_before": roll.current_length,
            "cut_qty": cut_qty,
            "balance_after": roll.current_length - cut_qty,
            "cost_per_meter": roll.cost_per_meter,
            "total_cost": cut_qty * roll.cost_per_meter,
            "remarks": item.get("remarks")
        })
    
    doc.insert()
    
    if data.get("submit", False):
        doc.submit()
    
    frappe.db.commit()
    
    return {
        "cutting_no": doc.name,
        "status": "Submitted" if doc.docstatus == 1 else "Draft",
        "total_cut_qty": doc.total_cut_qty,
        "total_cost": doc.total_cost,
        "message": _("Sample cutting created successfully")
    }


@frappe.whitelist()
def create_retail_sale(data):
    """
    Create a retail cutting sale
    
    Args:
        data: dict with sale details
            - roll_number: Roll to cut from
            - cut_qty: Quantity to sell in meters
            - rate: Price per meter
            - sale_type: Cash or Credit
            - customer: Customer for credit sales
    
    Returns:
        dict: Created sale info
    """
    if isinstance(data, str):
        data = json.loads(data)
    
    roll_number = data.get("roll_number")
    cut_qty = flt(data.get("cut_qty"))
    rate = flt(data.get("rate"))
    sale_type = data.get("sale_type", "Cash")
    
    if not roll_number:
        frappe.throw(_("Roll number is required"))
    
    if cut_qty <= 0:
        frappe.throw(_("Quantity must be positive"))
    
    if rate <= 0:
        frappe.throw(_("Rate must be positive"))
    
    roll = frappe.get_doc("Fabric Roll", roll_number)
    
    if cut_qty > roll.available_length:
        frappe.throw(
            _("Cannot sell {0}m from roll {1}. Available: {2}m").format(
                cut_qty, roll_number, roll.available_length
            )
        )
    
    if sale_type == "Credit" and not data.get("customer"):
        frappe.throw(_("Customer is required for credit sales"))
    
    amount = cut_qty * rate
    discount_percentage = flt(data.get("discount_percentage"))
    discount_amount = flt(data.get("discount_amount"))
    
    if discount_percentage:
        discount_amount = amount * discount_percentage / 100
    
    net_amount = amount - discount_amount
    tax_amount = flt(data.get("tax_amount"))
    grand_total = net_amount + tax_amount
    
    doc = frappe.new_doc("Retail Cutting Sale")
    doc.posting_date = data.get("posting_date") or nowdate()
    doc.posting_time = data.get("posting_time") or nowtime()
    doc.roll_number = roll_number
    doc.item_code = roll.item_code
    doc.item_name = roll.item_name
    doc.color = roll.color
    doc.balance_before = roll.current_length
    doc.cut_qty = cut_qty
    doc.balance_after = roll.current_length - cut_qty
    doc.rate = rate
    doc.amount = amount
    doc.discount_percentage = discount_percentage
    doc.discount_amount = discount_amount
    doc.net_amount = net_amount
    doc.tax_amount = tax_amount
    doc.grand_total = grand_total
    doc.sale_type = sale_type
    doc.customer = data.get("customer")
    doc.warehouse = data.get("warehouse") or roll.warehouse
    doc.remarks = data.get("remarks")
    
    doc.insert()
    
    if data.get("submit", False):
        doc.submit()
    
    frappe.db.commit()
    
    return {
        "sale_no": doc.name,
        "roll_number": doc.roll_number,
        "cut_qty": doc.cut_qty,
        "grand_total": doc.grand_total,
        "balance_after": doc.balance_after,
        "status": "Submitted" if doc.docstatus == 1 else "Draft",
        "message": _("Retail sale created successfully")
    }
