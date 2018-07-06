
from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document
from frappe.share import add
from frappe import _, throw


@frappe.whitelist()
def get_data_screen(id, type, module, project):
	if type == "screen":
		data = frappe.db.get_list("Screen",
				filters={"name": id},
				fields=['screen_name', 'project', 'module', 'status', 'task', 'screen_description', 'development_task', 'testing_task'])
		screenshots = frappe.db.get_list("File", 
						fields=['file_url'],
						filters={'attached_to_name': id}
						)
		functionality = frappe.db.get_list('Functionality',
						filters={'screen':id, 'module': module, 'project': project},
						fields=['subject','status','task','description','name']
						)

		functionality_names = []

		for x in functionality:
			functionality_names.append(x.name)

		checkpoints = frappe.db.get_list('Functional Check Points',
						filters={"parent": ["in", functionality_names]},
						fields=['subject','status','task']
						)
		
		functionality_task = []

		for x in functionality:
			functionality_task.append(x.task)

		checkpoints_tasks = []

		for y in checkpoints:
			checkpoints_tasks.append(y.task)

		tasks = []

		if data[0].task:
			tasks.append(data[0].task)
		if data[0].development_task:
			tasks.append(data[0].development_task)
		if data[0].testing_task:
			tasks.append(data[0].testing_task)

		if functionality_task:			
			for t in functionality_task:
				tasks.append(t)
		if checkpoints_tasks:
			for t in checkpoints_tasks:
				tasks.append(t)

		
		task_list = []

		for y in tasks:
			task_list.append({"name":y, "subject":frappe.db.get_value("Task", y, "subject"), "status":frappe.db.get_value("Task", y, "status")})

		bugs = frappe.db.get_list('Bug Sheet',
						filters={"project": project, "module": module, "screen": id},
						fields=['bug_title','name','category', 'priority', 'status', 'bug_description']
						)
		
	return {"data":data[0], "screenshots":screenshots,
			"functionality": functionality,"task_list": task_list, "bugs": bugs}

@frappe.whitelist()
def get_data_module(id, type, project):
	if type == "module":
		data = frappe.db.get_list("Module",
				filters={"name": id},
				fields=['module_name', 'project', 'status', 'task', 'module_description'])

		screenshots = frappe.db.get_list("File", 
						fields=['file_url'],
						filters={'attached_to_name': id}
						)

		functionality = frappe.db.get_list('Functionality',
						filters={'module': id, 'project': project},
						fields=['subject','status','task','description','name']
						)

		screens = frappe.db.get_list("Screen",
				filters={"project": project, "module": id},
				fields=['screen_name', 'project', 'module', 'status', 'task', 'screen_description', 'development_task', 'testing_task'])
	

		functionality_names = []

		for x in functionality:
			functionality_names.append(x.name)

		checkpoints = frappe.db.get_list('Functional Check Points',
						filters={"parent": ["in", functionality_names]},
						fields=['subject','status','task']
						)
		
		functionality_task = []

		for x in functionality:
			functionality_task.append(x.task)

		checkpoints_tasks = []

		for y in checkpoints:
			checkpoints_tasks.append(y.task)

		tasks = []
		if screens:
			for t in screens:
				tasks.append(t.task)
				tasks.append(t.development_task)
				tasks.append(t.testing_task)
				
		tasks.append(data[0].task)

		if functionality_task:			
			for t in functionality_task:
				tasks.append(t)
		if checkpoints_tasks:
			for t in checkpoints_tasks:
				tasks.append(t)

		
		task_list = []

		for y in tasks:
			task_list.append({"name":y, "subject":frappe.db.get_value("Task", y, "subject"), "status":frappe.db.get_value("Task", y, "status")})

		bugs = frappe.db.get_list('Bug Sheet',
						filters={"project": project, "module": id},
						fields=['bug_title','name','category', 'priority', 'status', 'bug_description']
						)
		
	return {"data":data[0], "screenshots":screenshots,
			"functionality": functionality,"task_list": task_list, "bugs": bugs}

@frappe.whitelist()
def get_data_project(id, type):
	if type == "project":
		data = frappe.db.get_list("Project",
				filters={"name": id},
				fields=['status', 'project_name', 'priority'])
		
		screenshots = frappe.db.get_list("File", 
						fields=['file_url'],
						filters={'attached_to_name': id}
						)

		modules = frappe.db.get_list("Module",
				filters={"project": id},
				fields=['module_name', 'project', 'status', 'task', 'module_description'])

		screens = frappe.db.get_list("Screen",
				filters={"project": id},
				fields=['screen_name', 'project', 'module', 'status', 'task', 'screen_description', 'development_task', 'testing_task'])
	
		functionality = frappe.db.get_list('Functionality',
						filters={'project': id},
						fields=['subject','status','task','description','name']
						)
		
		functionality_names = []

		for x in functionality:
			functionality_names.append(x.name)

		checkpoints = frappe.db.get_list('Functional Check Points',
						filters={"parent": ["in", functionality_names]},
						fields=['subject','status','task']
						)
		
		functionality_task = []

		for x in functionality:
			functionality_task.append(x.task)

		checkpoints_tasks = []

		for y in checkpoints:
			checkpoints_tasks.append(y.task)

		tasks = []

		if modules:
			for t in modules:
				tasks.append(t.task)

		if screens:
			for t in screens:
				tasks.append(t.task)
				tasks.append(t.development_task)
				tasks.append(t.testing_task)		

		if functionality_task:			
			for t in functionality_task:
				tasks.append(t)
		if checkpoints_tasks:
			for t in checkpoints_tasks:
				tasks.append(t)

		task_list = []

		for y in tasks:
			task_list.append({"name":y, "subject":frappe.db.get_value("Task", y, "subject"), "status":frappe.db.get_value("Task", y, "status")})

		bugs = frappe.db.get_list('Bug Sheet',
						filters={"project": id},
						fields=['bug_title','name','category', 'priority', 'status', 'bug_description']
						)
		
	return {"data":data[0], "screenshots":screenshots, "task_list": task_list, "bugs": bugs, "modules":modules, "screens":screens}




