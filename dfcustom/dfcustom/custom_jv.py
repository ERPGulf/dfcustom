from frappe.model.naming import make_autoname

def custom_name(doc, method):
    company_abbr = doc.company[:2].upper() 
    if doc.voucher_type == "Deferred Expense":
        prefix = f"ACE-{company_abbr}-"
    elif doc.voucher_type == "Deferred Revenue":
        prefix = f"ACR-{company_abbr}-"
    else:
        return 
    doc.naming_series = prefix + ".YYYY.-"

    
    doc.name = make_autoname(doc.naming_series)

