"""
QR Code Generator
=================
Functions for generating QR codes for rolls
"""

import frappe
from frappe import _
from frappe.utils import get_files_path
import os
import json
import base64


def generate_qr_code(data, size=200):
    """
    Generate QR code image
    
    Args:
        data: Data to encode
        size: Image size in pixels
    
    Returns:
        str: Base64 encoded image
    """
    try:
        import qrcode
        from io import BytesIO
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return f"data:image/png;base64,{img_str}"
    
    except ImportError:
        frappe.log_error("qrcode library not installed")
        return None


def generate_roll_qr(roll_number, include_details=False):
    """
    Generate QR code for a fabric roll
    
    Args:
        roll_number: Roll number
        include_details: Include additional roll data in QR
    
    Returns:
        str: Base64 encoded QR image
    """
    if include_details:
        roll = frappe.get_doc("Fabric Roll", roll_number)
        data = json.dumps({
            "roll": roll_number,
            "item": roll.item_code,
            "color": roll.color,
            "length": roll.current_length,
            "warehouse": roll.warehouse
        }, ensure_ascii=False)
    else:
        data = roll_number
    
    return generate_qr_code(data)


def save_roll_qr(roll_number):
    """
    Generate and save QR code file for a roll
    
    Args:
        roll_number: Roll number
    
    Returns:
        str: File path
    """
    qr_base64 = generate_roll_qr(roll_number)
    if not qr_base64:
        return None
    
    img_data = qr_base64.split(",")[1]
    img_bytes = base64.b64decode(img_data)
    
    file_name = f"roll_qr_{roll_number}.png"
    file_path = os.path.join(get_files_path(), file_name)
    
    with open(file_path, "wb") as f:
        f.write(img_bytes)
    
    file_doc = frappe.new_doc("File")
    file_doc.file_name = file_name
    file_doc.is_private = 0
    file_doc.file_url = f"/files/{file_name}"
    file_doc.attached_to_doctype = "Fabric Roll"
    file_doc.attached_to_name = roll_number
    file_doc.attached_to_field = "qr_code"
    file_doc.insert(ignore_permissions=True)
    
    return file_doc.file_url


def generate_batch_qr_labels(roll_numbers, template=None):
    """
    Generate QR labels for multiple rolls
    
    Args:
        roll_numbers: List of roll numbers
        template: Label template name
    
    Returns:
        list: Label data for printing
    """
    labels = []
    
    for roll_number in roll_numbers:
        roll = frappe.get_doc("Fabric Roll", roll_number)
        qr = generate_roll_qr(roll_number)
        
        labels.append({
            "roll_number": roll.roll_number,
            "item_code": roll.item_code,
            "item_name": roll.item_name,
            "color": roll.color,
            "color_name": roll.color_name,
            "batch_id": roll.batch_id,
            "current_length": roll.current_length,
            "warehouse": roll.warehouse,
            "bin_location": roll.bin_location,
            "qr_code": qr,
            "barcode": roll.barcode or roll.roll_number
        })
    
    return labels
