"""
Roll Transfer DocType
=====================
Transfer rolls between warehouses
"""

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class RollTransfer(Document):
    def validate(self):
        self.validate_warehouses()
        self.validate_items()
        self.calculate_totals()
    
    def validate_warehouses(self):
        if self.from_warehouse == self.to_warehouse:
            frappe.throw(_("Source and target warehouse cannot be the same"))
    
    def validate_items(self):
        for item in self.items:
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            if roll.warehouse != self.from_warehouse:
                frappe.throw(
                    _("Roll {0} is not in warehouse {1}").format(
                        item.roll_number, self.from_warehouse
                    )
                )
    
    def calculate_totals(self):
        self.total_rolls = len(self.items)
        self.total_meters = sum(flt(d.current_length) for d in self.items)
    
    def before_save(self):
        if not self.posting_time:
            self.posting_time = frappe.utils.nowtime()
        
        for item in self.items:
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            item.item_code = roll.item_code
            item.item_name = roll.item_name
            item.color = roll.color
            item.current_length = roll.current_length
            item.from_bin = roll.bin_location
    
    def on_submit(self):
        self.transfer_rolls()
    
    def on_cancel(self):
        self.reverse_transfer()
    
    def transfer_rolls(self):
        for item in self.items:
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            roll.transfer(
                target_warehouse=self.to_warehouse,
                bin_location=item.to_bin,
                remarks=f"مناقلة - {self.name}"
            )
    
    def reverse_transfer(self):
        for item in self.items:
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            roll.warehouse = self.from_warehouse
            roll.bin_location = item.from_bin
            roll.save()


def on_submit(doc, method):
    pass

def on_cancel(doc, method):
    pass
