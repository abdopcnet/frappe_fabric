"""
Roll Management APIs
====================
APIs for managing fabric rolls - get, search, update
"""

import frappe
from frappe import _
from frappe.utils import now_datetime, flt
import json


@frappe.whitelist()
def get_roll(roll_number):
    """
    Get roll details by roll number
    
    Args:
        roll_number: Roll number or QR code
    
    Returns:
        dict: Roll details with movements
    
    API: GET /api/method/frappe_fabric.api.roll.get_roll
    """
    if not roll_number:
        frappe.throw(_("Roll number is required"))
    
    if not frappe.db.exists("Fabric Roll", roll_number):
        frappe.throw(_("Roll {0} not found").format(roll_number))
    
    roll = frappe.get_doc("Fabric Roll", roll_number)
    
    # Get recent movements
    movements = frappe.get_all(
        "Roll Movement",
        filters={"roll_number": roll_number},
        fields=["name", "posting_date", "posting_time", "movement_type", 
                "quantity", "balance_before", "balance_after", "warehouse",
                "reference_doctype", "reference_name", "remarks"],
        order_by="posting_date desc, posting_time desc",
        limit=20
    )
    
    return {
        "roll_number": roll.roll_number,
        "item_code": roll.item_code,
        "item_name": roll.item_name,
        "color": roll.color,
        "color_name": roll.color_name,
        "batch_id": roll.batch_id,
        "original_length": roll.original_length,
        "current_length": roll.current_length,
        "consumed_length": roll.consumed_length,
        "reserved_length": roll.reserved_length,
        "available_length": roll.available_length,
        "warehouse": roll.warehouse,
        "bin_location": roll.bin_location,
        "status": roll.status,
        "cost_per_meter": roll.cost_per_meter,
        "total_cost": roll.total_cost,
        "qr_code": roll.qr_code,
        "receipt_date": roll.receipt_date,
        "last_movement_date": roll.last_movement_date,
        "movements": movements
    }


@frappe.whitelist()
def get_roll_by_qr(qr_code):
    """
    Get roll by QR code scan
    
    Args:
        qr_code: Scanned QR code value
    
    Returns:
        dict: Roll details
    """
    if not qr_code:
        frappe.throw(_("QR code is required"))
    
    roll_number = frappe.db.get_value("Fabric Roll", {"roll_number": qr_code})
    
    if not roll_number:
        roll_number = frappe.db.get_value("Fabric Roll", {"barcode": qr_code})
    
    if not roll_number:
        frappe.throw(_("Roll not found for QR code: {0}").format(qr_code))
    
    return get_roll(roll_number)


@frappe.whitelist()
def search_rolls(filters=None, search_term=None, page=1, page_size=20):
    """
    Search rolls with filters
    
    Args:
        filters: dict of filters (item_code, warehouse, status, etc.)
        search_term: Search in roll_number, item_name
        page: Page number
        page_size: Results per page
    
    Returns:
        dict: Results with pagination info
    """
    if isinstance(filters, str):
        filters = json.loads(filters)
    
    filters = filters or {}
    conditions = []
    values = {}
    
    if filters.get("item_code"):
        conditions.append("item_code = %(item_code)s")
        values["item_code"] = filters["item_code"]
    
    if filters.get("warehouse"):
        conditions.append("warehouse = %(warehouse)s")
        values["warehouse"] = filters["warehouse"]
    
    if filters.get("status"):
        conditions.append("status = %(status)s")
        values["status"] = filters["status"]
    
    if filters.get("min_length"):
        conditions.append("current_length >= %(min_length)s")
        values["min_length"] = flt(filters["min_length"])
    
    if search_term:
        conditions.append("(roll_number LIKE %(search)s OR item_name LIKE %(search)s)")
        values["search"] = f"%{search_term}%"
    
    if "is_active" not in filters:
        conditions.append("is_active = 1")
    
    where_clause = " AND ".join(conditions) if conditions else "1=1"
    
    total = frappe.db.sql(f"""
        SELECT COUNT(*) FROM "tabFabric Roll"
        WHERE {where_clause}
    """, values)[0][0]
    
    offset = (int(page) - 1) * int(page_size)
    
    rolls = frappe.db.sql(f"""
        SELECT 
            roll_number, item_code, item_name, color, color_name,
            batch_id, original_length, current_length, available_length,
            warehouse, bin_location, status, cost_per_meter
        FROM "tabFabric Roll"
        WHERE {where_clause}
        ORDER BY modified DESC
        LIMIT %(limit)s OFFSET %(offset)s
    """, {**values, "limit": int(page_size), "offset": offset}, as_dict=True)
    
    return {
        "data": rolls,
        "total": total,
        "page": int(page),
        "page_size": int(page_size),
        "total_pages": (total + int(page_size) - 1) // int(page_size)
    }


@frappe.whitelist()
def update_roll_location(roll_number, warehouse, bin_location=None):
    """
    Update roll warehouse location
    
    Args:
        roll_number: Roll number
        warehouse: Target warehouse
        bin_location: Bin/shelf location
    
    Returns:
        dict: Updated roll info
    """
    if not roll_number:
        frappe.throw(_("Roll number is required"))
    
    roll = frappe.get_doc("Fabric Roll", roll_number)
    old_warehouse = roll.warehouse
    
    roll.warehouse = warehouse
    if bin_location:
        roll.bin_location = bin_location
    
    roll.save()
    
    # Create movement record
    movement = frappe.new_doc("Roll Movement")
    movement.roll_number = roll_number
    movement.posting_date = frappe.utils.nowdate()
    movement.posting_time = frappe.utils.nowtime()
    movement.movement_type = "Transfer"
    movement.quantity = 0
    movement.warehouse = old_warehouse
    movement.warehouse_to = warehouse
    movement.bin_location_to = bin_location
    movement.balance_before = roll.current_length
    movement.balance_after = roll.current_length
    movement.insert()
    
    frappe.db.commit()
    
    return {
        "roll_number": roll.roll_number,
        "warehouse": roll.warehouse,
        "bin_location": roll.bin_location,
        "message": _("Location updated successfully")
    }


@frappe.whitelist()
def reserve_roll(roll_number, reserve_length, reference_doctype=None, reference_name=None):
    """
    Reserve quantity from a roll
    
    Args:
        roll_number: Roll number
        reserve_length: Length to reserve
        reference_doctype: Linked document type
        reference_name: Linked document name
    
    Returns:
        dict: Updated roll info
    """
    if not roll_number:
        frappe.throw(_("Roll number is required"))
    
    reserve_length = flt(reserve_length)
    if reserve_length <= 0:
        frappe.throw(_("Reserve length must be positive"))
    
    roll = frappe.get_doc("Fabric Roll", roll_number)
    
    if reserve_length > roll.available_length:
        frappe.throw(
            _("Cannot reserve {0}m. Available: {1}m").format(
                reserve_length, roll.available_length
            )
        )
    
    roll.reserved_length = flt(roll.reserved_length) + reserve_length
    roll.available_length = roll.current_length - roll.reserved_length
    
    if roll.reserved_length > 0:
        roll.status = "Reserved"
    
    roll.save()
    frappe.db.commit()
    
    return {
        "roll_number": roll.roll_number,
        "reserved_length": roll.reserved_length,
        "available_length": roll.available_length,
        "status": roll.status,
        "message": _("Roll reserved successfully")
    }
