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
						frappe.msgprint(__("Thanks for your acceptanance."));
						$('#acceptbtn').text('Accepted');
						$('#acceptbtn').addClass('disabled');
						$('#rejectbtn').hide();


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
						frappe.msgprint(__("Thanks for your response."));
						$('#rejectbtn').text('Rejected');
						$('#rejectbtn').addClass('disabled');
						$('#rejectbtn').hide();

					}
				});	
}

$(document).ready(function(){
    var a = $('#maindivi').height();
    $('#sidedive').css('height', a+100);
});

