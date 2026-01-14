"""
Fabric Item DocType
===================
Master data for fabric items
"""

import frappe
from frappe import _
from frappe.model.document import Document


class FabricItem(Document):
    def validate(self):
        self.validate_rates()
        self.validate_dimensions()
    
    def validate_rates(self):
        if self.standard_rate and self.standard_rate < 0:
            frappe.throw(_("Standard Rate cannot be negative"))
        if self.valuation_rate and self.valuation_rate < 0:
            frappe.throw(_("Valuation Rate cannot be negative"))
    
    def validate_dimensions(self):
        if self.width and self.width < 0:
            frappe.throw(_("Width cannot be negative"))
        if self.weight_per_meter and self.weight_per_meter < 0:
            frappe.throw(_("Weight per meter cannot be negative"))
    
    def before_save(self):
        if not self.item_name_en:
            self.item_name_en = self.item_name
    
    def on_update(self):
        self.update_roll_rates()
    
    def update_roll_rates(self):
        if self.has_value_changed("valuation_rate"):
            frappe.db.sql("""
                UPDATE tabFabric Roll
                SET cost_per_meter = %s
                WHERE item_code = %s AND docstatus = 0
            """, (self.valuation_rate, self.name))
    
    @frappe.whitelist()
    def get_available_rolls(self, warehouse=None):
        filters = {
            "item_code": self.name,
            "status": ["in", ["Available", "Reserved"]],
            "is_active": 1
        }
        if warehouse:
            filters["warehouse"] = warehouse
        return frappe.get_all(
            "Fabric Roll",
            filters=filters,
            fields=["name", "roll_number", "current_length", "available_length", 
                    "warehouse", "bin_location", "status", "color"]
        )
    
    @frappe.whitelist()
    def get_stock_summary(self):
        return frappe.db.sql("""
            SELECT 
                warehouse,
                COUNT(*) as roll_count,
                SUM(current_length) as total_length,
                SUM(available_length) as available_length,
                SUM(reserved_length) as reserved_length
            FROM tabFabric Roll
            WHERE item_code = %s AND is_active = 1
            GROUP BY warehouse
        """, self.name, as_dict=True)
