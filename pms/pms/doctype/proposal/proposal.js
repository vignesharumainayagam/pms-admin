// Copyright (c) 2018, Valiant Systems  and contributors
// For license information, please see license.txt

frappe.ui.form.on('Proposal', {
	sub_total: function(frm) {
		frm.set_value('tax', frm.doc.sub_total*18/100);
	},
	tax: function(frm) {
		frm.set_value('grand_total', frm.doc.sub_total + frm.doc.tax)
	},
	product: function(frm) {
			frappe.call({
				method: "pms.pms.doctype.proposal.proposal.get_data_from_template",
				args: {
					template: frm.doc.product,
				},
				callback: function(r) {
					$.each(r.message, function(i, d) {
						var row = frappe.model.add_child(frm.doc, "Proposal Data", "contents");
						
						row.title = d.title
						row.content = d.content

					});
			 		refresh_field("contents");

							}
			});
	}
});

frappe.ui.form.on("Proposal Child", "rate", function multiply_quantity(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	var total = 0;
	for(var i in frm.doc.items){
		total += frm.doc.items[i].rate
	}
	frm.set_value("sub_total",total);
});   
	
frappe.ui.form.on("Proposal Child", "qty", function (frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	frappe.model.set_value(cdt, cdn, "rate", d.qty * d.price);

}); 	

frappe.ui.form.on("Proposal Child", "price", function (frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	frappe.model.set_value(cdt, cdn, "rate", d.qty * d.price);

});