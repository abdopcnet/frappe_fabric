"""
Reports APIs
============
APIs for generating fabric reports
"""

import frappe
from frappe import _
from frappe.utils import flt, nowdate


@frappe.whitelist()
def get_stock_balance(filters=None):
    """
    Get roll stock balance report
    
    Args:
        filters: dict with filters
            - warehouse: Filter by warehouse
            - item_code: Filter by item
            - as_on_date: Stock as on date
    
    Returns:
        dict: Stock balance data
    """
    filters = filters or {}
    
    conditions = ["fr.is_active = 1", "fr.status != 'Exhausted'"]
    values = {}
    
    if filters.get("warehouse"):
        conditions.append("fr.warehouse = %(warehouse)s")
        values["warehouse"] = filters["warehouse"]
    
    if filters.get("item_code"):
        conditions.append("fr.item_code = %(item_code)s")
        values["item_code"] = filters["item_code"]
    
    where_clause = " AND ".join(conditions)
    
    data = frappe.db.sql(f"""
        SELECT 
            fr.warehouse,
            fr.item_code,
            fi.item_name,
            fr.color,
            COUNT(fr.name) as total_rolls,
            SUM(fr.current_length) as total_length,
            SUM(fr.available_length) as available_length,
            SUM(fr.reserved_length) as reserved_length,
            SUM(fr.total_cost) as total_value
        FROM "tabFabric Roll" fr
        LEFT JOIN tabFabric Item fi ON fr.item_code = fi.name
        WHERE {where_clause}
        GROUP BY fr.warehouse, fr.item_code, fr.color
        ORDER BY fr.warehouse, fr.item_code, fr.color
    """, values, as_dict=True)
    
    summary = {
        "total_rolls": sum(d.total_rolls for d in data),
        "total_length": sum(d.total_length for d in data),
        "total_value": sum(d.total_value or 0 for d in data)
    }
    
    return {
        "data": data,
        "summary": summary
    }


@frappe.whitelist()
def get_movement_history(filters=None):
    """
    Get roll movement history
    
    Args:
        filters: dict with filters
            - roll_number: Specific roll
            - from_date: Start date
            - to_date: End date
            - movement_type: Type of movement
    
    Returns:
        dict: Movement history data
    """
    filters = filters or {}
    
    conditions = []
    values = {}
    
    if filters.get("roll_number"):
        conditions.append("rm.roll_number = %(roll_number)s")
        values["roll_number"] = filters["roll_number"]
    
    if filters.get("from_date"):
        conditions.append("rm.posting_date >= %(from_date)s")
        values["from_date"] = filters["from_date"]
    
    if filters.get("to_date"):
        conditions.append("rm.posting_date <= %(to_date)s")
        values["to_date"] = filters["to_date"]
    
    if filters.get("movement_type"):
        conditions.append("rm.movement_type = %(movement_type)s")
        values["movement_type"] = filters["movement_type"]
    
    where_clause = " AND ".join(conditions) if conditions else "1=1"
    
    data = frappe.db.sql(f"""
        SELECT 
            rm.name,
            rm.posting_date,
            rm.posting_time,
            rm.roll_number,
            rm.item_code,
            rm.movement_type,
            rm.quantity,
            rm.balance_before,
            rm.balance_after,
            rm.warehouse,
            rm.warehouse_to,
            rm.reference_doctype,
            rm.reference_name,
            rm.remarks
        FROM tabRoll Movement rm
        WHERE {where_clause}
        ORDER BY rm.posting_date DESC, rm.posting_time DESC
        LIMIT 500
    """, values, as_dict=True)
    
    return {
        "data": data,
        "count": len(data)
    }


@frappe.whitelist()
def get_cutting_summary(filters=None):
    """
    Get cutting summary report
    
    Args:
        filters: dict with filters
            - from_date: Start date
            - to_date: End date
            - purpose: Cutting purpose
    
    Returns:
        dict: Cutting summary data
    """
    filters = filters or {}
    
    from_date = filters.get("from_date") or frappe.utils.add_months(nowdate(), -1)
    to_date = filters.get("to_date") or nowdate()
    
    sample_cutting = frappe.db.sql("""
        SELECT 
            sc.purpose,
            COUNT(sc.name) as count,
            SUM(sc.total_cut_qty) as total_qty,
            SUM(sc.total_cost) as total_cost
        FROM tabSample Cutting sc
        WHERE sc.docstatus = 1
          AND sc.posting_date BETWEEN %(from_date)s AND %(to_date)s
        GROUP BY sc.purpose
    """, {"from_date": from_date, "to_date": to_date}, as_dict=True)
    
    retail_sales = frappe.db.sql("""
        SELECT 
            rcs.sale_type,
            COUNT(rcs.name) as count,
            SUM(rcs.cut_qty) as total_qty,
            SUM(rcs.grand_total) as total_revenue
        FROM tabRetail Cutting Sale rcs
        WHERE rcs.docstatus = 1
          AND rcs.posting_date BETWEEN %(from_date)s AND %(to_date)s
        GROUP BY rcs.sale_type
    """, {"from_date": from_date, "to_date": to_date}, as_dict=True)
    
    return {
        "sample_cutting": sample_cutting,
        "retail_sales": retail_sales,
        "period": {"from_date": from_date, "to_date": to_date}
    }
