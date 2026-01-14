"""
Roll Utilities
==============
Helper functions for roll management
"""

import frappe
from frappe import _
from frappe.utils import flt, cint, nowdate, nowtime


def get_roll_balance(roll_number):
    """
    Get current balance of a roll
    
    Args:
        roll_number: Roll number
    
    Returns:
        dict: Balance info
    """
    roll = frappe.get_doc("Fabric Roll", roll_number)
    
    return {
        "roll_number": roll.roll_number,
        "original_length": roll.original_length,
        "current_length": roll.current_length,
        "consumed_length": roll.consumed_length,
        "reserved_length": roll.reserved_length,
        "available_length": roll.available_length,
        "status": roll.status
    }


def deduct_from_roll(roll_number, quantity, movement_type, reference_doctype=None, reference_name=None, warehouse=None, remarks=None):
    """
    Deduct quantity from a roll and create movement record
    
    Args:
        roll_number: Roll number
        quantity: Quantity to deduct
        movement_type: Type of movement
        reference_doctype: Linked document type
        reference_name: Linked document name
        warehouse: Warehouse (optional)
        remarks: Notes
    
    Returns:
        dict: Updated roll info
    """
    quantity = flt(quantity)
    if quantity <= 0:
        frappe.throw(_("Quantity must be positive"))
    
    roll = frappe.get_doc("Fabric Roll", roll_number)
    
    if quantity > roll.available_length:
        frappe.throw(
            _("Cannot deduct {0}m from roll {1}. Available: {2}m").format(
                quantity, roll_number, roll.available_length
            )
        )
    
    balance_before = roll.current_length
    
    roll.consumed_length = flt(roll.consumed_length) + quantity
    roll.current_length = roll.original_length - roll.consumed_length
    roll.available_length = roll.current_length - flt(roll.reserved_length)
    
    if roll.current_length <= 0:
        roll.status = "Exhausted"
        roll.is_active = 0
    
    roll.last_movement_date = frappe.utils.now_datetime()
    roll.save()
    
    # Create movement record
    movement = frappe.new_doc("Roll Movement")
    movement.roll_number = roll_number
    movement.item_code = roll.item_code
    movement.posting_date = nowdate()
    movement.posting_time = nowtime()
    movement.movement_type = movement_type
    movement.quantity = quantity
    movement.balance_before = balance_before
    movement.balance_after = roll.current_length
    movement.warehouse = warehouse or roll.warehouse
    movement.reference_doctype = reference_doctype
    movement.reference_name = reference_name
    movement.remarks = remarks
    movement.insert()
    
    frappe.db.commit()
    
    return {
        "roll_number": roll.roll_number,
        "quantity_deducted": quantity,
        "balance_before": balance_before,
        "balance_after": roll.current_length,
        "available_length": roll.available_length,
        "status": roll.status,
        "movement_id": movement.name
    }


def release_reservation(roll_number, release_length, reference_doctype=None, reference_name=None):
    """
    Release reserved quantity from a roll
    
    Args:
        roll_number: Roll number
        release_length: Length to release
        reference_doctype: Original reservation document type
        reference_name: Original reservation document name
    
    Returns:
        dict: Updated roll info
    """
    release_length = flt(release_length)
    if release_length <= 0:
        frappe.throw(_("Release length must be positive"))
    
    roll = frappe.get_doc("Fabric Roll", roll_number)
    
    if release_length > roll.reserved_length:
        release_length = roll.reserved_length
    
    roll.reserved_length = flt(roll.reserved_length) - release_length
    roll.available_length = roll.current_length - roll.reserved_length
    
    if roll.reserved_length <= 0 and roll.status == "Reserved":
        roll.status = "Available"
    
    roll.save()
    frappe.db.commit()
    
    return {
        "roll_number": roll.roll_number,
        "released_length": release_length,
        "reserved_length": roll.reserved_length,
        "available_length": roll.available_length,
        "status": roll.status
    }


def transfer_roll(roll_number, target_warehouse, bin_location=None, remarks=None):
    """
    Transfer roll to another warehouse
    
    Args:
        roll_number: Roll number
        target_warehouse: Target warehouse
        bin_location: New bin location
        remarks: Transfer notes
    
    Returns:
        dict: Updated roll info
    """
    roll = frappe.get_doc("Fabric Roll", roll_number)
    
    source_warehouse = roll.warehouse
    source_bin = roll.bin_location
    
    roll.warehouse = target_warehouse
    roll.bin_location = bin_location
    roll.last_movement_date = frappe.utils.now_datetime()
    roll.save()
    
    # Create movement record
    movement = frappe.new_doc("Roll Movement")
    movement.roll_number = roll_number
    movement.item_code = roll.item_code
    movement.posting_date = nowdate()
    movement.posting_time = nowtime()
    movement.movement_type = "Transfer"
    movement.quantity = 0
    movement.balance_before = roll.current_length
    movement.balance_after = roll.current_length
    movement.warehouse = source_warehouse
    movement.bin_location = source_bin
    movement.warehouse_to = target_warehouse
    movement.bin_location_to = bin_location
    movement.remarks = remarks
    movement.insert()
    
    frappe.db.commit()
    
    return {
        "roll_number": roll.roll_number,
        "from_warehouse": source_warehouse,
        "to_warehouse": target_warehouse,
        "bin_location": bin_location,
        "movement_id": movement.name
    }
