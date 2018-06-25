from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Requiment Gathering & Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Project"
				},				
				{
					"type": "doctype",
					"name": "Module"
				},
				{
					"type": "doctype",
					"name": "Screen"
				},
				{
					"type": "doctype",
					"name": "Functionality"
				}
			]
		},
		{
			"label": _("Bug & Error Tracking "),
			"items": [
				{
					"type": "doctype",
					"name": "Bug Sheet",
					"label": "Bug Sheet"
				},			
				{
					"type": "doctype",
					"name": "Test Case"
				},
		 	# 	{
				# 	"type": "page",
				# 	"name": "pms",
				# 	"label": _("PMS"),
				# 	"description": _("PMS")
				# },
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Field Type"
				},			
				{
					"type": "doctype",
					"name": "Validation"
				}
			]
		},		
	] 