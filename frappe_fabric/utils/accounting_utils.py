"""
Accounting Utilities
====================
Helper functions for accounting entries
"""

import frappe
from frappe import _
from frappe.utils import flt


def create_gl_entry(account, debit=0, credit=0, against_account=None, voucher_type=None, voucher_no=None, cost_center=None, remarks=None, posting_date=None, company=None):
    """
    Create a General Ledger entry
    
    Args:
        account: Account name
        debit: Debit amount
        credit: Credit amount
        against_account: Against account
        voucher_type: Document type
        voucher_no: Document name
        cost_center: Cost center
        remarks: Entry remarks
        posting_date: Posting date
        company: Company name
    
    Returns:
        str: GL Entry name
    """
    if not company:
        company = frappe.defaults.get_user_default("Company")
    
    if not posting_date:
        posting_date = frappe.utils.nowdate()
    
    gl_entry = frappe.new_doc("GL Entry")
    gl_entry.posting_date = posting_date
    gl_entry.account = account
    gl_entry.debit = flt(debit)
    gl_entry.credit = flt(credit)
    gl_entry.against = against_account
    gl_entry.voucher_type = voucher_type
    gl_entry.voucher_no = voucher_no
    gl_entry.cost_center = cost_center
    gl_entry.remarks = remarks
    gl_entry.company = company
    gl_entry.insert()
    
    return gl_entry.name


def create_sample_cutting_entries(cutting_doc):
    """
    Create accounting entries for sample cutting
    
    Args:
        cutting_doc: Sample Cutting document
    
    Returns:
        list: Created GL Entry names
    """
    if not cutting_doc.expense_account:
        return []
    
    company = frappe.defaults.get_user_default("Company")
    entries = []
    
    # Get stock account
    stock_account = frappe.get_value("Company", company, "default_inventory_account")
    if not stock_account:
        frappe.throw(_("Please set default inventory account in Company settings"))
    
    total_cost = flt(cutting_doc.total_cost)
    
    if total_cost <= 0:
        return []
    
    # Debit expense account
    debit_entry = create_gl_entry(
        account=cutting_doc.expense_account,
        debit=total_cost,
        against_account=stock_account,
        voucher_type="Sample Cutting",
        voucher_no=cutting_doc.name,
        cost_center=cutting_doc.cost_center,
        remarks=f"Sample cutting - {cutting_doc.purpose}",
        posting_date=cutting_doc.posting_date,
        company=company
    )
    entries.append(debit_entry)
    
    # Credit stock account
    credit_entry = create_gl_entry(
        account=stock_account,
        credit=total_cost,
        against_account=cutting_doc.expense_account,
        voucher_type="Sample Cutting",
        voucher_no=cutting_doc.name,
        cost_center=cutting_doc.cost_center,
        remarks=f"Sample cutting - {cutting_doc.purpose}",
        posting_date=cutting_doc.posting_date,
        company=company
    )
    entries.append(credit_entry)
    
    return entries


def create_retail_sale_entries(sale_doc):
    """
    Create accounting entries for retail cutting sale
    
    Args:
        sale_doc: Retail Cutting Sale document
    
    Returns:
        list: Created GL Entry names
    """
    company = frappe.defaults.get_user_default("Company")
    entries = []
    
    # Get accounts
    income_account = sale_doc.income_account or frappe.get_value("Company", company, "default_income_account")
    stock_account = frappe.get_value("Company", company, "default_inventory_account")
    
    if sale_doc.sale_type == "Cash":
        debit_account = sale_doc.debit_account or frappe.get_value("Company", company, "default_cash_account")
    else:
        # Credit sale - debit receivables
        debit_account = frappe.get_value("Company", company, "default_receivable_account")
    
    if not all([income_account, stock_account, debit_account]):
        frappe.throw(_("Please set default accounts in Company settings"))
    
    # 1. Debit cash/receivables, Credit income
    debit_entry = create_gl_entry(
        account=debit_account,
        debit=flt(sale_doc.grand_total),
        against_account=income_account,
        voucher_type="Retail Cutting Sale",
        voucher_no=sale_doc.name,
        cost_center=sale_doc.cost_center,
        remarks=f"Retail sale - {sale_doc.roll_number}",
        posting_date=sale_doc.posting_date,
        company=company
    )
    entries.append(debit_entry)
    
    credit_entry = create_gl_entry(
        account=income_account,
        credit=flt(sale_doc.grand_total),
        against_account=debit_account,
        voucher_type="Retail Cutting Sale",
        voucher_no=sale_doc.name,
        cost_center=sale_doc.cost_center,
        remarks=f"Retail sale - {sale_doc.roll_number}",
        posting_date=sale_doc.posting_date,
        company=company
    )
    entries.append(credit_entry)
    
    # 2. Debit COGS, Credit stock
    roll = frappe.get_doc("Fabric Roll", sale_doc.roll_number)
    cost_of_goods = flt(sale_doc.cut_qty) * flt(roll.cost_per_meter)
    
    cogs_account = frappe.get_value("Company", company, "default_expense_account")
    if cogs_account and cost_of_goods > 0:
        cogs_debit = create_gl_entry(
            account=cogs_account,
            debit=cost_of_goods,
            against_account=stock_account,
            voucher_type="Retail Cutting Sale",
            voucher_no=sale_doc.name,
            cost_center=sale_doc.cost_center,
            remarks=f"Cost of goods - {sale_doc.roll_number}",
            posting_date=sale_doc.posting_date,
            company=company
        )
        entries.append(cogs_debit)
        
        stock_credit = create_gl_entry(
            account=stock_account,
            credit=cost_of_goods,
            against_account=cogs_account,
            voucher_type="Retail Cutting Sale",
            voucher_no=sale_doc.name,
            cost_center=sale_doc.cost_center,
            remarks=f"Stock reduction - {sale_doc.roll_number}",
            posting_date=sale_doc.posting_date,
            company=company
        )
        entries.append(stock_credit)
    
    return entries
