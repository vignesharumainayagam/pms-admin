// Copyright (c) 2017, Valiant Systems  and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bug Sheet', {
	onload: function(frm) {
    console.log(frm)
	}
});


frappe.ui.form.on("Bug Sheet", "onload", function(frm) {

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

frappe.ui.form.on("Bug Sheet", "validate", function(frm){
var data = frappe.datetime.now_date();
if (frm.doc.status == "Fixed") {
cur_frm.set_value("fixed_on", data);
}
else if (frm.doc.status == "Verified") {
cur_frm.set_value("verified_on", data);	
}
});


frappe.ui.form.on("Bug Sheet", "assign", function(frm){
var arr = frm.doc.table_11;
for(var i=0; i<arr.length; i++){
  $.ajax({
  url : window.location.origin+"/api/resource/DocShare",
  dataType: 'text',
  type: 'POST',
  contentType: 'application/json',
  data : JSON.stringify( {
  "user" : arr[i].assign_to,
  "share_doctype" : frm.doc.doctype,
  "share_name" : frm.doc.name,
  "read" : 1,
  "write" : 1,
  "share" : 1
  }
  ),
  beforeSend: function(xhr){
  xhr.setRequestHeader(
  'X-Frappe-CSRF-Token', frappe.csrf_token
  );
  },success: function(data){
  console.log(data);
  }, error: function(error){
  console.log(error);
  }
  });
}
});



