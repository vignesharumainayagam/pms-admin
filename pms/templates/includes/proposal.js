var id = $('#page_id').html();
function accept() {

			frappe.call({
					method: "frappe.client.set_value",
					args: {
						doctype: "Proposal",
						name: id,
						fieldname: "status",
						value: "Accept",
					},
					freeze: true,
					callback: (r) => {
						frappe.msgprint(__("Successfully Accepted"));
						$('#acceptbtn').hide();
						$('#rejectbtn').show();

					}
				});
}

function reject() {
			frappe.call({
					method: "frappe.client.set_value",
					args: {
						doctype: "Proposal",
						name: id,
						fieldname: "status",
						value: "Reject",
					},
					freeze: true,
					callback: (r) => {
						frappe.msgprint(__("Successfully Rejected"));
						$('#rejectbtn').hide();
						$('#acceptbtn').show();

					}
				});	
}

$(document).ready(function(){
    var a = $('#maindivi').height();
    $('#sidedive').css('height', a+100);
});

