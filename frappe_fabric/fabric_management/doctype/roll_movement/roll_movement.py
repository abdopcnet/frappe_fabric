import frappe
from frappe.model.document import Document

class RollMovement(Document):
    def before_save(self):
        if not self.posting_time:
            self.posting_time = frappe.utils.nowtime()
        if not self.created_by:
            self.created_by = frappe.session.user
