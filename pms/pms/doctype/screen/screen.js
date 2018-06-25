// Copyright (c) 2017, Valiant Systems  and contributors
// For license information, please see license.txt

frappe.ui.form.on('Screen', {
	refresh: function(frm) {

	}
});
frappe.ui.form.on("Screen", "onload", function(frm) {

  cur_frm.set_query("module", function() {
      return {
          "filters": {
              "project": frm.doc.project
          }
      };
  });

  
});
