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

@frappe.whitelist()
def senddailytask(allow_guest=True):	
	projects = frappe.db.get_list("Project", 
					fields=['project_name', 'status', 'name', 'priority'],
					filters={'status': "Open"},
					limit_page_length=200
					)	

	for x in projects:
		opentasks = frappe.db.get_list("Task", 
							fields=['name'],
							filters={'project': x.name, 'status': ["!=", "Closed"]},
							limit_page_length=200
							)
		if opentasks: 
			x.opentasks = len(opentasks)
		else:
			x.opentasks = 0	

		closedtasks = frappe.db.get_list("Task", 
							fields=['name'],
							filters={'project': x.name, 'status': 'Closed'},
							limit_page_length=200
							)
		if closedtasks: 
			x.closedtasks = len(closedtasks)
		else:
			x.closedtasks = 0	
		
		openbugs = frappe.db.get_list("Bug Sheet", 
							fields=['name'],
							filters={'project': x.name, 'status': ["in", "Closed"]},
							limit_page_length=200
							)
		if openbugs: 
			x.openbugs = len(openbugs)
		else:
			x.openbugs = 0	

		
		closedbugs = frappe.db.get_list("Bug Sheet", 
							fields=['name'],
							filters={'project': x.name, 'status': 'Closed'},
							limit_page_length=200
							)
		if closedbugs: 
			x.closedbugs = len(closedbugs)
		else:
			x.closedbugs = 0	

	table = '<table cellpading="5" style="border-collapse: collapse;" border="1"><tr><th>Project Name</th><th>Open Tasks</th><th>Closed Tasks</th><th>Open Bugs</th><th>Closed Bugs</th></tr>'
	for y in projects:
		table = table + '<tr><td>'+str(y.project_name)+'</td><td>'+str(y.opentasks)+'</td><td>'+str(y.closedtasks)+'</td><td>'+str(y.openbugs)+'</td><td>'+str(y.closedbugs)+'</td></tr>'

	table = table + '</table>'	
	data = 'sample'

	frappe.sendmail(recipients=['vigneshwaran@valiantsystems.com'],
		sender = "Testing Valiant2 <testing.valiant2@gmail.com>",
		message=table,
		subject=data)
	return None
















