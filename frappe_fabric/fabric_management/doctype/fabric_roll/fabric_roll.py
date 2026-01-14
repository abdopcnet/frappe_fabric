"""
Fabric Roll DocType
===================
Individual fabric roll tracking
"""

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, nowdate, now_datetime


class FabricRoll(Document):
    def autoname(self):
        if not self.roll_number:
            self.roll_number = self.name
    
    def validate(self):
        self.validate_lengths()
        self.calculate_totals()
        self.validate_warehouse()
    
    def validate_lengths(self):
        if self.original_length <= 0:
            frappe.throw(_("Original length must be greater than zero"))
        if flt(self.current_length) < 0:
            frappe.throw(_("Current length cannot be negative"))
        if flt(self.consumed_length) < 0:
            frappe.throw(_("Consumed length cannot be negative"))
        if flt(self.reserved_length) < 0:
            frappe.throw(_("Reserved length cannot be negative"))
    
    def calculate_totals(self):
        if not self.current_length:
            self.current_length = self.original_length
        self.available_length = flt(self.current_length) - flt(self.reserved_length)
        if self.available_length < 0:
            self.available_length = 0
        if self.cost_per_meter:
            self.total_cost = flt(self.current_length) * flt(self.cost_per_meter)
    
    def validate_warehouse(self):
        if self.warehouse and not frappe.db.exists("Warehouse", self.warehouse):
            frappe.throw(_("Warehouse {0} does not exist").format(self.warehouse))
    
    def before_save(self):
        if not self.roll_number:
            self.roll_number = self.name
        if not self.receipt_date:
            self.receipt_date = nowdate()
        self.update_status()
        if not self.qr_code:
            self.generate_qr_code()
    
    def update_status(self):
        if self.current_length <= 0:
            self.status = "Exhausted"
            self.is_active = 0
        elif self.reserved_length > 0:
            self.status = "Reserved"
        elif self.status == "Exhausted":
            self.status = "Available"
    
    def generate_qr_code(self):
        try:
            from frappe_fabric.utils.qr_generator import save_roll_qr
            qr_url = save_roll_qr(self.roll_number or self.name)
            if qr_url:
                self.qr_code = qr_url
        except Exception:
            pass
    
    @frappe.whitelist()
    def get_movements(self, limit=20):
        return frappe.get_all(
            "Roll Movement",
            filters={"roll_number": self.name},
            fields=["name", "posting_date", "posting_time", "movement_type",
                    "quantity", "balance_before", "balance_after", "warehouse",
                    "reference_doctype", "reference_name", "remarks"],
            order_by="posting_date desc, posting_time desc",
            limit=limit
        )
    
    @frappe.whitelist()
    def reserve(self, length, reference_doctype=None, reference_name=None):
        length = flt(length)
        if length <= 0:
            frappe.throw(_("Reserve length must be positive"))
        if length > self.available_length:
            frappe.throw(_("Cannot reserve {0}m. Available: {1}m").format(length, self.available_length))
        self.reserved_length = flt(self.reserved_length) + length
        self.available_length = flt(self.current_length) - self.reserved_length
        self.status = "Reserved"
        self.save()
        return {"reserved_length": self.reserved_length, "available_length": self.available_length}
    
    @frappe.whitelist()
    def deduct(self, quantity, movement_type, reference_doctype=None, reference_name=None, remarks=None):
        quantity = flt(quantity)
        if quantity <= 0:
            frappe.throw(_("Quantity must be positive"))
        if quantity > self.available_length:
            frappe.throw(_("Cannot deduct {0}m. Available: {1}m").format(quantity, self.available_length))
        balance_before = self.current_length
        self.consumed_length = flt(self.consumed_length) + quantity
        self.current_length = flt(self.original_length) - flt(self.consumed_length)
        self.available_length = flt(self.current_length) - flt(self.reserved_length)
        if self.current_length <= 0:
            self.status = "Exhausted"
            self.is_active = 0
        self.last_movement_date = now_datetime()
        self.last_movement_type = movement_type
        self.save()
        movement = frappe.new_doc("Roll Movement")
        movement.roll_number = self.name
        movement.item_code = self.item_code
        movement.posting_date = nowdate()
        movement.posting_time = frappe.utils.nowtime()
        movement.movement_type = movement_type
        movement.quantity = quantity
        movement.balance_before = balance_before
        movement.balance_after = self.current_length
        movement.warehouse = self.warehouse
        movement.reference_doctype = reference_doctype
        movement.reference_name = reference_name
        movement.remarks = remarks
        movement.insert(ignore_permissions=True)
        return {"deducted": quantity, "current_length": self.current_length, "available_length": self.available_length, "movement": movement.name}


def before_save(doc, method):
    pass

def on_update(doc, method):
    pass
