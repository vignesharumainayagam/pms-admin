# -*- coding: utf-8 -*-
# Copyright (c) 2017, Valiant Systems  and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document
from frappe.share import add
from frappe import _, throw

class BugSheet(Document):
	pass

@frappe.whitelist()
def get_users(names):
	names = json.loads(names)
	name = tuple(names)
	params = {'l': name}
	projects = frappe.db.sql('''select distinct project from `tabBug Sheet` where name in %(l)s''',params)
	projects = tuple(projects)
	params1 = {'u': projects}
	users = frappe.db.sql('''select distinct user from `tabDocShare` where share_name in %(u)s''',params1)
	return users


@frappe.whitelist()
def post(user, doctype, names):
	names = json.loads(names)
	users = json.loads(user)
	for x in users:
		if x[1] == 1:
			for name in names:
				add(doctype, name, user=x[0], read=1, write=1, share=0, everyone=0, flags=None, notify=0)
	return users
