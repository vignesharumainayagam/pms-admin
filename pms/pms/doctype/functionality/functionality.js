// Copyright (c) 2018, Valiant Systems  and contributors
// For license information, please see license.txt

frappe.ui.form.on('Functionality', {
	refresh: function(frm) {

	}
});
frappe.ui.form.on("Functionality", "onload", function(frm) {

  cur_frm.set_query("module", function() {
      return {
          "filters": {
              "project": frm.doc.project
          }
      };
  });

  cur_frm.set_query("screen", function() {
      return {
          "filters": {
              "project": frm.doc.project,
              "module": frm.doc.screen
          }
      };
  });
  
});
