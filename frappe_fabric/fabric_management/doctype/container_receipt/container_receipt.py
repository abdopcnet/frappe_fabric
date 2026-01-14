"""
Container Receipt DocType
=========================
Manage container/shipment receipts
"""

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, cint


class ContainerReceipt(Document):
    def validate(self):
        self.calculate_totals()
        self.calculate_variance()
    
    def calculate_totals(self):
        self.total_expected_rolls = sum(cint(d.expected_rolls) for d in self.expected_items)
        self.total_expected_meters = sum(flt(d.expected_meters) for d in self.expected_items)
        self.total_received_rolls = len(self.received_rolls)
        self.total_received_meters = sum(flt(d.scanned_length) for d in self.received_rolls)
    
    def calculate_variance(self):
        self.roll_variance = self.total_received_rolls - self.total_expected_rolls
        self.meter_variance = flt(self.total_received_meters) - flt(self.total_expected_meters)
    
    def before_save(self):
        if not self.posting_time:
            self.posting_time = frappe.utils.nowtime()
        if self.total_received_rolls > 0:
            if self.total_received_rolls >= self.total_expected_rolls:
                self.status = "Completed"
            else:
                self.status = "In Progress"
    
    def on_submit(self):
        self.status = "Completed"
        self.update_expected_items_received()
    
    def on_cancel(self):
        self.status = "Cancelled"
        for row in self.received_rolls:
            if row.roll_number and frappe.db.exists("Fabric Roll", row.roll_number):
                roll = frappe.get_doc("Fabric Roll", row.roll_number)
                roll.is_active = 0
                roll.status = "Cancelled"
                roll.save(ignore_permissions=True)
    
    def update_expected_items_received(self):
        for expected in self.expected_items:
            received_rolls = 0
            received_meters = 0
            for roll in self.received_rolls:
                if roll.item_code == expected.item_code and (not expected.color or roll.color == expected.color):
                    received_rolls += 1
                    received_meters += flt(roll.scanned_length)
            expected.received_rolls = received_rolls
            expected.received_meters = received_meters
    
    @frappe.whitelist()
    def scan_roll(self, roll_data):
        if isinstance(roll_data, str):
            import json
            roll_data = json.loads(roll_data)
        
        item_code = roll_data.get("item_code")
        if not item_code:
            frappe.throw(_("Item code is required"))
        
        scanned_length = flt(roll_data.get("scanned_length"))
        if scanned_length <= 0:
            frappe.throw(_("Scanned length must be positive"))
        
        from frappe.utils import nowdate
        import random
        import string
        date_part = nowdate().replace("-", "")
        count = frappe.db.count("Fabric Roll", {"creation": [">=", nowdate()]}) + 1
        suffix = ''.join(random.choices(string.ascii_uppercase, k=4))
        roll_number = f"ROLL-{date_part}-{count:04d}-{suffix}"
        
        roll = frappe.new_doc("Fabric Roll")
        roll.roll_number = roll_number
        roll.item_code = item_code
        roll.color = roll_data.get("color")
        roll.original_length = scanned_length
        roll.current_length = scanned_length
        roll.available_length = scanned_length
        roll.warehouse = self.warehouse
        roll.bin_location = roll_data.get("bin_location")
        roll.container_receipt = self.name
        roll.supplier = self.supplier
        roll.receipt_date = self.posting_date
        roll.status = "Available"
        roll.insert(ignore_permissions=True)
        
        self.append("received_rolls", {
            "roll_number": roll_number,
            "item_code": item_code,
            "color": roll_data.get("color"),
            "scanned_length": scanned_length,
            "bin_location": roll_data.get("bin_location"),
            "scan_time": frappe.utils.now_datetime()
        })
        
        self.calculate_totals()
        self.calculate_variance()
        self.save()
        
        return {
            "roll_number": roll_number,
            "item_code": item_code,
            "scanned_length": scanned_length,
            "total_received_rolls": self.total_received_rolls,
            "total_received_meters": self.total_received_meters
        }


def on_submit(doc, method):
    pass

def on_cancel(doc, method):
    pass
