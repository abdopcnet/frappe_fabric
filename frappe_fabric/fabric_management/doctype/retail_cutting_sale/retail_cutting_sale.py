"""
Retail Cutting Sale DocType
===========================
Point of sale for fabric cutting
"""

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class RetailCuttingSale(Document):
    def validate(self):
        self.validate_roll()
        self.validate_customer()
        self.calculate_totals()
    
    def validate_roll(self):
        if not self.roll_number:
            frappe.throw(_("Roll number is required"))
        
        roll = frappe.get_doc("Fabric Roll", self.roll_number)
        if flt(self.cut_qty) > roll.available_length:
            frappe.throw(
                _("Cannot sell {0}m from roll {1}. Available: {2}m").format(
                    self.cut_qty, self.roll_number, roll.available_length
                )
            )
    
    def validate_customer(self):
        if self.sale_type == "Credit" and not self.customer:
            frappe.throw(_("Customer is required for credit sales"))
    
    def calculate_totals(self):
        self.amount = flt(self.cut_qty) * flt(self.rate)
        
        if flt(self.discount_percentage) > 0:
            self.discount_amount = self.amount * flt(self.discount_percentage) / 100
        
        self.net_amount = self.amount - flt(self.discount_amount)
        self.grand_total = self.net_amount + flt(self.tax_amount)
        
        # Calculate cost and profit
        roll = frappe.get_doc("Fabric Roll", self.roll_number)
        self.cost_per_meter = roll.cost_per_meter
        self.total_cost = flt(self.cut_qty) * flt(roll.cost_per_meter)
        self.gross_profit = self.net_amount - self.total_cost
    
    def before_save(self):
        if not self.invoice_no:
            self.invoice_no = self.name
        if not self.posting_time:
            self.posting_time = frappe.utils.nowtime()
        
        roll = frappe.get_doc("Fabric Roll", self.roll_number)
        self.item_code = roll.item_code
        self.item_name = roll.item_name
        self.color = roll.color
        self.balance_before = roll.current_length
        self.balance_after = roll.current_length - flt(self.cut_qty)
        self.warehouse = self.warehouse or roll.warehouse
    
    def on_submit(self):
        self.update_roll()
        self.create_accounting_entries()
    
    def on_cancel(self):
        self.reverse_roll()
        self.cancel_accounting_entries()
    
    def update_roll(self):
        roll = frappe.get_doc("Fabric Roll", self.roll_number)
        roll.deduct(
            quantity=self.cut_qty,
            movement_type="Retail Sale",
            reference_doctype="Retail Cutting Sale",
            reference_name=self.name,
            remarks=f"بيع مفرد - {self.customer_name or 'نقدي'}"
        )
    
    def reverse_roll(self):
        roll = frappe.get_doc("Fabric Roll", self.roll_number)
        roll.consumed_length = flt(roll.consumed_length) - flt(self.cut_qty)
        roll.current_length = roll.original_length - roll.consumed_length
        roll.available_length = roll.current_length - flt(roll.reserved_length)
        if roll.current_length > 0 and roll.status == "Exhausted":
            roll.status = "Available"
            roll.is_active = 1
        roll.save()
    
    def create_accounting_entries(self):
        from frappe_fabric.utils.accounting_utils import create_retail_sale_entries
        create_retail_sale_entries(self)
    
    def cancel_accounting_entries(self):
        frappe.db.delete("GL Entry", {
            "voucher_type": "Retail Cutting Sale",
            "voucher_no": self.name
        })


def on_submit(doc, method):
    pass

def on_cancel(doc, method):
    pass
