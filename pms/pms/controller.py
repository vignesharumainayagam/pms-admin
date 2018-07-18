from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, cstr
from frappe.email.doctype.email_group.email_group import add_subscribers
from frappe.utils import (add_days, getdate, formatdate, date_diff,
	add_years, get_timestamp, nowdate, flt, add_months, get_last_day)


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



@frappe.whitelist()
def senddailytimesheet(allow_guest=True):	
	Employee = frappe.db.get_list("Employee", 
					fields=['employee_name', 'name'],
					filters={'status': "Active"},
					limit_page_length=200
					)	

	for x in Employee:
		x.Timesheet = frappe.db.get_list("Timesheet", 
							fields=['name'],
							filters={'employee': x.name, 'start_date': ["=", nowdate()]},
							limit_page_length=200
							)

		for y in x.Timesheet:
			y.tasks = frappe.db.get_list("Timesheet Detail", 
								fields=['name', 'project', 'task', 'hours', 'from_time', 'to_time'],
								filters={'parent': y.name},
								limit_page_length=200
								)
			for q in z.tasks:
				q.tasks_details = frappe.db.get_list("Task", 
							fields=['subject', 'status', 'priority', 'description', 'name'],
							filters={'name': z.name},
							limit_page_length=200
							)

	# table = '<table cellpading="5" style="border-collapse: collapse;" border="1"><tr><th>Project Name</th><th>Open Tasks</th><th>Closed Tasks</th><th>Open Bugs</th><th>Closed Bugs</th></tr>'
	# for y in projects:
	# 	table = table + '<tr><td>'+str(y.project_name)+'</td><td>'+str(y.opentasks)+'</td><td>'+str(y.closedtasks)+'</td><td>'+str(y.openbugs)+'</td><td>'+str(y.closedbugs)+'</td></tr>'

	# table = table + '</table>'	
	# data = 'sample'

	# frappe.sendmail(recipients=['vigneshwaran@valiantsystems.com'],
	# 	sender = "Testing Valiant2 <testing.valiant2@gmail.com>",
	# 	message=table,
	# 	subject=data)
	return Employee
















