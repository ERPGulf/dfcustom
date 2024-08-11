import frappe
from frappe.model.document import Document
from erpnext.accounts.deferred_revenue import book_deferred_income_or_expense
from erpnext.accounts.deferred_revenue import send_mail
from frappe.utils import (
	add_days,
	add_months,
	today,
)


class Custom_ProcessDeferredAccounting(Document):
	def on_submit(self):
		conditions = _build_conditions(self.type, self.account, self.company)
		if self.type == "Income":
			_convert_deferred_revenue_to_income(self.name, self.start_date, self.end_date, conditions,self.invoice_number)
		else:
			_convert_deferred_expense_to_expense(self.name, self.start_date, self.end_date, conditions,self.invoice_number)

def _build_conditions(process_type, account, company, invoice_number=None):
	conditions = ""
	deferred_account = (
		"item.deferred_revenue_account" if process_type == "Income" else "item.deferred_expense_account"
	)

	if account:
		conditions += f"AND {deferred_account}='{account}'"
	elif company:
		conditions += f"AND p.company = {frappe.db.escape(company)}"

	if invoice_number:
		conditions += f" AND item.parent = '{invoice_number}'"

	return conditions

def _convert_deferred_expense_to_expense(deferred_process, start_date=None, end_date=None, conditions="",invoice_number=""):
	# book the expense/income on the last day, but it will be trigger on the 1st of month at 12:00 AM

	if not start_date:
		start_date = add_months(today(), -1)
	if not end_date:
		end_date = add_days(today(), -1)

	conditions += _build_conditions("Expense", None, None, invoice_number)

	# check for the purchase invoice for which GL entries have to be done
	invoices = frappe.db.sql_list(
		f"""
		SELECT DISTINCT item.parent
		FROM `tabPurchase Invoice Item` item, `tabPurchase Invoice` p
		WHERE item.service_start_date <= %s 
		  AND item.service_end_date >= %s
		  AND item.enable_deferred_expense = 1 
		  AND item.parent = p.name
		  AND item.docstatus = 1 
		  AND IFNULL(item.amount, 0) > 0
		  {conditions}
		""",
		(end_date, start_date),
	)  # nosec

	for invoice in invoices:
		doc = frappe.get_doc("Purchase Invoice", invoice)
		book_deferred_income_or_expense(doc, deferred_process, end_date)

	if frappe.flags.deferred_accounting_error:
		send_mail(deferred_process)



def _convert_deferred_revenue_to_income(deferred_process, start_date=None, end_date=None, conditions="",invoice_number=""):
	# book the expense/income on the last day, but it will be trigger on the 1st of month at 12:00 AM
	if not start_date:
		start_date = add_months(today(), -1)
	if not end_date:
		end_date = add_days(today(), -1)

	conditions += _build_conditions("Income", None, None, invoice_number)

	# check for the sales invoice for which GL entries have to be done
	invoices = frappe.db.sql_list(
		f"""
		SELECT DISTINCT item.parent
		FROM `tabSales Invoice Item` item, `tabSales Invoice` p
		WHERE item.service_start_date <= %s 
		  AND item.service_end_date >= %s
		  AND item.enable_deferred_revenue = 1 
		  AND item.parent = p.name
		  AND item.docstatus = 1 
		  AND IFNULL(item.amount, 0) > 0
		  {conditions}
		""",
		(end_date, start_date),
	)  # nosec

	for invoice in invoices:
		doc = frappe.get_doc("Sales Invoice", invoice)
		book_deferred_income_or_expense(doc, deferred_process, end_date)

	if frappe.flags.deferred_accounting_error:
		send_mail(deferred_process)


