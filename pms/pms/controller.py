from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, cstr
from frappe.email.doctype.email_group.email_group import add_subscribers



@frappe.whitelist()
def create_project_task(doc):
	pass
	# Dis= frappe.get_doc({
	# 	"doctype": "Employee",
	# 	"employee_name": employee_name,
	# 	"company":company,
	# 	"date_of_joining":date_of_joining,
	# 	"date_of_birth":date_of_birth,
	# 	"gender":gender,
	# 	"status": status,
	# 	"employment_type":employment_type,
	# 	"cell_number":cell_number,
	# 	"personal_email":personal_email,
	# 	"current_address":current_address,
	# 	"leave_type": leave_type,
	# 	"roll_no":roll_no
	# }).insert()	  	
	# return Dis