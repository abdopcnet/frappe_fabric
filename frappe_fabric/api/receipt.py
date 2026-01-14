"""
Container Receipt APIs
======================
APIs for managing container/shipment receipts
"""

import frappe
from frappe import _
from frappe.utils import nowdate, nowtime, flt, cint
import json


@frappe.whitelist()
def create_container_receipt(data):
    """
    Create a new container receipt
    
    Args:
        data: dict with receipt details
            - container_number: Container/shipment number
            - supplier: Supplier name
            - warehouse: Target warehouse
            - expected_items: List of expected items
    
    Returns:
        dict: Created receipt info
    """
    if isinstance(data, str):
        data = json.loads(data)
    
    if not data.get("container_number"):
        frappe.throw(_("Container number is required"))
    
    if not data.get("warehouse"):
        frappe.throw(_("Warehouse is required"))
    
    doc = frappe.new_doc("Container Receipt")
    doc.container_number = data.get("container_number")
    doc.supplier = data.get("supplier")
    doc.warehouse = data.get("warehouse")
    doc.posting_date = data.get("posting_date") or nowdate()
    doc.posting_time = data.get("posting_time") or nowtime()
    doc.purchase_order = data.get("purchase_order")
    doc.bill_of_lading = data.get("bill_of_lading")
    doc.shipping_company = data.get("shipping_company")
    doc.remarks = data.get("remarks")
    
    for item in data.get("expected_items", []):
        doc.append("expected_items", {
            "item_code": item.get("item_code"),
            "expected_rolls": cint(item.get("expected_rolls")),
            "expected_meters": flt(item.get("expected_meters")),
            "color": item.get("color"),
            "remarks": item.get("remarks")
        })
    
    doc.insert()
    frappe.db.commit()
    
    return {
        "receipt_no": doc.name,
        "container_number": doc.container_number,
        "status": doc.status,
        "total_expected_rolls": doc.total_expected_rolls,
        "total_expected_meters": doc.total_expected_meters,
        "message": _("Container receipt created successfully")
    }


@frappe.whitelist()
def get_container_receipt(receipt_no):
    """
    Get container receipt details
    
    Args:
        receipt_no: Receipt document name
    
    Returns:
        dict: Receipt details with items and rolls
    """
    if not receipt_no:
        frappe.throw(_("Receipt number is required"))
    
    if not frappe.db.exists("Container Receipt", receipt_no):
        frappe.throw(_("Receipt {0} not found").format(receipt_no))
    
    doc = frappe.get_doc("Container Receipt", receipt_no)
    
    return {
        "receipt_no": doc.name,
        "container_number": doc.container_number,
        "supplier": doc.supplier,
        "warehouse": doc.warehouse,
        "posting_date": doc.posting_date,
        "status": doc.status,
        "total_expected_rolls": doc.total_expected_rolls,
        "total_received_rolls": doc.total_received_rolls,
        "total_expected_meters": doc.total_expected_meters,
        "total_received_meters": doc.total_received_meters,
        "expected_items": [
            {
                "item_code": item.item_code,
                "expected_rolls": item.expected_rolls,
                "expected_meters": item.expected_meters,
                "received_rolls": item.received_rolls,
                "received_meters": item.received_meters,
                "color": item.color
            }
            for item in doc.expected_items
        ],
        "received_rolls": [
            {
                "roll_number": roll.roll_number,
                "item_code": roll.item_code,
                "color": roll.color,
                "scanned_length": roll.scanned_length,
                "bin_location": roll.bin_location
            }
            for roll in doc.received_rolls
        ]
    }


@frappe.whitelist()
def scan_roll(receipt_no, roll_data=None):
    """
    Scan/add a roll to the receipt
    
    Args:
        receipt_no: Receipt document name
        roll_data: dict for new rolls:
            - item_code: Fabric item
            - color: Color
            - scanned_length: Measured length
            - bin_location: Storage location
    
    Returns:
        dict: Scanned roll info with progress
    """
    if isinstance(roll_data, str):
        roll_data = json.loads(roll_data)
    
    roll_data = roll_data or {}
    
    if not receipt_no:
        frappe.throw(_("Receipt number is required"))
    
    doc = frappe.get_doc("Container Receipt", receipt_no)
    
    if doc.docstatus == 1:
        frappe.throw(_("Cannot add rolls to a submitted receipt"))
    
    item_code = roll_data.get("item_code")
    if not item_code:
        frappe.throw(_("Item code is required"))
    
    scanned_length = flt(roll_data.get("scanned_length"))
    if scanned_length <= 0:
        frappe.throw(_("Scanned length must be positive"))
    
    # Generate roll number
    from frappe.utils import nowdate
    date_part = nowdate().replace("-", "")
    count = frappe.db.count("Fabric Roll", {"creation": [">=", nowdate()]}) + 1
    import random
    import string
    suffix = ''.join(random.choices(string.ascii_uppercase, k=4))
    roll_number = f"ROLL-{date_part}-{count:04d}-{suffix}"
    
    # Create fabric roll
    roll = frappe.new_doc("Fabric Roll")
    roll.roll_number = roll_number
    roll.item_code = item_code
    roll.color = roll_data.get("color")
    roll.original_length = scanned_length
    roll.current_length = scanned_length
    roll.available_length = scanned_length
    roll.warehouse = doc.warehouse
    roll.bin_location = roll_data.get("bin_location")
    roll.receipt_date = doc.posting_date
    roll.status = "Available"
    roll.insert()
    
    # Add to receipt
    doc.append("received_rolls", {
        "roll_number": roll_number,
        "item_code": item_code,
        "color": roll_data.get("color"),
        "scanned_length": scanned_length,
        "bin_location": roll_data.get("bin_location"),
        "scan_time": frappe.utils.now_datetime()
    })
    doc.save()
    
    frappe.db.commit()
    
    return {
        "roll_number": roll_number,
        "item_code": item_code,
        "scanned_length": scanned_length,
        "total_received_rolls": doc.total_received_rolls,
        "total_received_meters": doc.total_received_meters,
        "message": _("Roll scanned successfully")
    }
