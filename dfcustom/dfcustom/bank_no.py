from erpnext.accounts.doctype.account.account import get_account_autoname
import frappe
from frappe.utils.nestedset import NestedSet


class Custom_Account(NestedSet):
    def autoname(self):

        if self.parent_account:
            parent_account_number = frappe.db.get_value("Account", self.parent_account, "account_number")
            if not parent_account_number:
                frappe.throw("Parent account does not have an account number")

            prefix = int(parent_account_number)
            starting_value = 10

            child_accounts = frappe.get_all(
                "Account",
                filters={"parent_account": self.parent_account, "is_group": 0},
                fields=["account_number"],
                order_by="account_number desc"
            )

            valid_account_numbers = [int(account['account_number']) for account in child_accounts if account['account_number']]

            if valid_account_numbers:
                last_account_number = max(valid_account_numbers)
                new_account_number = last_account_number + 1
            else:
                new_account_number = prefix + starting_value

            self.account_number = str(new_account_number)

        self.name = get_account_autoname(self.account_number, self.account_name, self.company)

    