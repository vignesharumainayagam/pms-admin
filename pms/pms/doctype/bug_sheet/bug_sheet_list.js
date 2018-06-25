
frappe.listview_settings['Bug Sheet'] = {
	add_fields: ["status", "priority"],
	onload: function(listview) {
		// console.log(listview)
		// listview.page.fields_dict.module.get_query = function(doc) {
		// 	return {filters: { project: listview.page.fields_dict.project.value}}
		// }
		// listview.page.fields_dict.screen.get_query = function(doc) {
		// 	return {filters: { project: listview.page.fields_dict.project.value, module: listview.page.fields_dict.module.value}}
		// }
	 //    var zTreeObj;
	 //   	// zTree configuration information, refer to API documentation (setting details)
		// function setRenameBtn(treeId, treeNode) {
		// 	return !treeNode.isParent;
		// }
		// var setting = {	
		// 	edit: {
		// 		enable: true,
		// 		drag: {
		// 			isCopy: false,
		// 			isMove: true
		// 		}
		// 	}	
		// };
	 //   // zTree data attributes, refer to the API documentation (treeNode data details)
	 //   var zNodes = [
	 //   {"name":"Project 1", "open":"true", "children":[
	 //      {"name":"Module 1", "open":"true", "children":[
	 //      		{"name":"Screen 1"}, {"name":"Screen 2"}]}, {"name":"Module 2", "open": "true"}]},
	 //   {"name":"Project 2", "open":"true", "children":[
	 //      {"name":"Module 1"}, {"name":"Module 2"}]}
	 //   ];
  //  $(document).ready(function(){
	 //  $(".filter_list").html('<ul id="treeDemo" class="ztree"></ul>');
  //     zTreeObj = $.fn.zTree.init($("#treeDemo"), setting, zNodes);
  //  });
		// // listview.page.add_menu_item(__("Share Bugs"), function() {
		// listview.page.add_action_icon("fa fa-share-alt", function() {	
		// var checked_bugs = listview.get_checked_items(true);
		// if(checked_bugs.length > 0){		
		// 	    frappe.call({
		// 	        method: "pms.pms.doctype.bug_sheet.bug_sheet.get_users",
		// 	        args:{
		// 			"names": checked_bugs, 
		// 			},
		// 	        callback: function(r) {
		// 	        	var arr = [];
		// 	        	for (var i = 0; i < r.message.length; i++) {
		// 	        		if (r.message[i].name != "Administrator" && r.message[i].name != "Guest") {
		// 	        		arr.push({
		// 								"label": r.message[i][0],
		// 								"fieldname": r.message[i][0],
		// 								"fieldtype": "Check"
		// 							})
		// 	        		}
		// 	        	}
		// 	            var d = new frappe.ui.Dialog({
		// 	                title: __('Share Bugs'),
		// 					fields: arr,                
		// 					primary_action: function() {
		// 						var obj = d.get_values();
		// 						var result = Object.keys(obj).map(function(key) {
		// 						  return [(key), obj[key]];
		// 						});
		// 						console.log(result)
		// 						var method = "pms.pms.doctype.bug_sheet.bug_sheet.post";
		// 						listview.call_for_selected_items(method, {"user": result, "doctype": cur_list.doctype});
		// 						d.hide();
		// 					},
		// 					primary_action_label: __('Share Bugs')                
		// 	            });
		// 	            d.show();


		// 	        }
		// 	    });
		// 	}
		// 	else{
		// 		frappe.msgprint("Please Select the Bugs to be shared")
		// 	}
		// });
	},
	get_indicator: function(doc) {
		if(doc.status=="Fixed") {
			return [__("Fixed"), "orange"];
		} else if(doc.status=="Verified") {
			return [__("Verified"), "green"];
		} else if(doc.status=="Open") {
			return [__("Open"), "red"];
		} else if(doc.status=="Re-open") {
			return [__("Re-open"), "red"];
		} else if(doc.status=="Closed") {
			return [__("Closed"), "blue"];
		}
		if(doc.priority=="High") {
			return [__("High"), "red"];
		} else if(doc.priority=="Medium") {
			return [__("Medium"), "black"];
		} else if(doc.priority=="Low") {
			return [__("Low"), "green"];
		}

	}

};


