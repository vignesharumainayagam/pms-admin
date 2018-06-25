frappe.listview_settings['Bug Sheet'] = {
	add_fields: ["status"],
	onload: function(listview) {

	},
	get_indicator: function(doc) {
		// if(doc.status=="Fixed") {
		// 	return [__("Fixed"), "orange"];
		// } else if(doc.status=="Verified") {
		// 	return [__("Verified"), "green"];
		// } else if(doc.status=="Open") {
		// 	return [__("Open"), "red"];
		// } else if(doc.status=="Re-open") {
		// 	return [__("Re-open"), "red"];
		// } else if(doc.status=="Closed") {
		// 	return [__("Closed"), "blue"];
		// }
		// if(doc.priority=="High") {
		// 	return [__("High"), "red"];
		// } else if(doc.priority=="Medium") {
		// 	return [__("Medium"), "black"];
		// } else if(doc.priority=="Low") {
		// 	return [__("Low"), "green"];
		// }

	}

};


