import frappe
from frappe.model.document import Document

class FabricBatch(Document):
    def autoname(self):
        if not self.batch_id:
            self.batch_id = self.name
    
    def validate(self):
        self.calculate_totals()
    
    def calculate_totals(self):
        if self.name:
            data = frappe.db.sql("""
                SELECT COUNT(*) as rolls, SUM(original_length) as length
                FROM tabFabric Roll
                WHERE batch_id = %s
            """, self.name, as_dict=True)[0]
            self.total_rolls = data.rolls or 0
            self.total_length = data.length or 0
