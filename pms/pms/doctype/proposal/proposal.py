# -*- coding: utf-8 -*-
# Copyright (c) 2018, Valiant Systems  and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import add_days, cint, cstr, flt, getdate, rounded, date_diff, money_in_words
from frappe.model.naming import make_autoname
from frappe.utils import random_string

class Proposal(WebsiteGenerator):
	pass
	def validate(self):
		if not self.route:
			self.route = 'proposal/'+random_string(6)
		
	def autoname(self):
		self.name = make_autoname('Proposal.#####')

	def on_update(self):
		if self.route:
			pass
		elif self.route -- None:
			self.route = 'proposal/'+random_string(6)

@frappe.whitelist()
def get_data_from_template(template):
	data = frappe.db.get_list('Proposal Data',
			fields = ['title', 'content'],
			filters = {'parent': template},
			order_by = "idx")

	data1 = frappe.db.get_list('Proposal Samples',
			fields = ['image', 'url'],
			filters = {'parent': template},
			order_by = "idx")
	return data,data1

@frappe.whitelist()
def get_items_from_template(template,currency):
	data = frappe.db.get_list('Proposal Child',
			fields = ['item', 'description', 'price', 'qty', 'rate', 'currency'],
			filters = {'parent': template, 'currency': currency},
			order_by = "idx")

	return data