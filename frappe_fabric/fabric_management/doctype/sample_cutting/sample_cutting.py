"""
Sample Cutting DocType
======================
Track sample cutting from fabric rolls
"""

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class SampleCutting(Document):
    def validate(self):
        self.validate_items()
        self.calculate_totals()
    
    def validate_items(self):
        for item in self.items:
            if flt(item.cut_qty) <= 0:
                frappe.throw(_("Cut quantity must be positive for all items"))
            
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            if flt(item.cut_qty) > roll.available_length:
                frappe.throw(
                    _("Cannot cut {0}m from roll {1}. Available: {2}m").format(
                        item.cut_qty, item.roll_number, roll.available_length
                    )
                )
    
    def calculate_totals(self):
        self.total_cut_qty = sum(flt(d.cut_qty) for d in self.items)
        self.total_cost = sum(flt(d.total_cost) for d in self.items)
    
    def before_save(self):
        if not self.cutting_no:
            self.cutting_no = self.name
        if not self.posting_time:
            self.posting_time = frappe.utils.nowtime()
        
        for item in self.items:
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            item.item_code = roll.item_code
            item.item_name = roll.item_name
            item.color = roll.color
            item.balance_before = roll.current_length
            item.balance_after = roll.current_length - flt(item.cut_qty)
            item.cost_per_meter = roll.cost_per_meter
            item.total_cost = flt(item.cut_qty) * flt(roll.cost_per_meter)
    
    def on_submit(self):
        self.update_rolls()
        self.create_accounting_entries()
    
    def on_cancel(self):
        self.reverse_rolls()
        self.cancel_accounting_entries()
    
    def update_rolls(self):
        for item in self.items:
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            roll.deduct(
                quantity=item.cut_qty,
                movement_type="Sample Cutting",
                reference_doctype="Sample Cutting",
                reference_name=self.name,
                remarks=f"قص عينات - {self.purpose}"
            )
    
    def reverse_rolls(self):
        # Reverse the cutting - add back to rolls
        for item in self.items:
            roll = frappe.get_doc("Fabric Roll", item.roll_number)
            roll.consumed_length = flt(roll.consumed_length) - flt(item.cut_qty)
            roll.current_length = roll.original_length - roll.consumed_length
            roll.available_length = roll.current_length - flt(roll.reserved_length)
            if roll.current_length > 0 and roll.status == "Exhausted":
                roll.status = "Available"
                roll.is_active = 1
            roll.save()
    
    def create_accounting_entries(self):
        from frappe_fabric.utils.accounting_utils import create_sample_cutting_entries
        create_sample_cutting_entries(self)
    
    def cancel_accounting_entries(self):
        # Delete GL entries for this document
        frappe.db.delete("GL Entry", {
            "voucher_type": "Sample Cutting",
            "voucher_no": self.name
        })


def on_submit(doc, method):
    pass

def on_cancel(doc, method):
    pass
