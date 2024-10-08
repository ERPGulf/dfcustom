app_name = "dfcustom"
app_title = "Dfcustom"
app_publisher = "ERPGulf"
app_description = "Defered customization"
app_email = "support@erpgulf.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dfcustom/css/dfcustom.css"
# app_include_js = "/assets/dfcustom/js/dfcustom.js"



# include js, css files in header of web template
# web_include_css = "/assets/dfcustom/css/dfcustom.css"
# web_include_js = "/assets/dfcustom/js/dfcustom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dfcustom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}


# # include js in doctype views

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "dfcustom/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dfcustom.utils.jinja_methods",
# 	"filters": "dfcustom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dfcustom.install.before_install"
# after_install = "dfcustom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dfcustom.uninstall.before_uninstall"
# after_uninstall = "dfcustom.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dfcustom.utils.before_app_install"
# after_app_install = "dfcustom.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dfcustom.utils.before_app_uninstall"
# after_app_uninstall = "dfcustom.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dfcustom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Process Deferred Accounting": "dfcustom.dfcustom.my_df.Custom_ProcessDeferredAccounting",
    "Account" : "dfcustom.dfcustom.bank_no.Custom_Account"
}




# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Journal Entry": {
		"before_insert": "dfcustom.dfcustom.custom_jv.custom_name",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dfcustom.tasks.all"
# 	],
# 	"daily": [
# 		"dfcustom.tasks.daily"
# 	],
# 	"hourly": [
# 		"dfcustom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dfcustom.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dfcustom.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dfcustom.install.before_tests"

# Overriding Methods
# ------------------------------

override_whitelisted_methods = {
    "erpnext.accounts.deferred_revenue.convert_deferred_expense_to_expense" : "df_custom.my_df._convert_deferred_expense_to_expense",
    "erpnext.accounts.deferred_revenue.convert_deferred_revenue_to_income" : "df_custom.my_df._convert_deferred_revenue_to_income",    
    "erpnext.accounts.deferred_revenue.build_conditions" : "df_custom.my_df._build_conditions",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dfcustom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["dfcustom.utils.before_request"]
# after_request = ["dfcustom.utils.after_request"]

# Job Events
# ----------
# before_job = ["dfcustom.utils.before_job"]
# after_job = ["dfcustom.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"dfcustom.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
fixtures = [ {"dt": "Custom Field","filters": [["module", "=", "dfcustom"]] }]
