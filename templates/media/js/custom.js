
/* Post Update */

$(document).ready(function() {

$.ajax({
	url: "/getdata/",
	type: "GET",
	dataType: 'html',
	success: function (html) {
				
				$('.append').html(html);
					},
		error: function () {

				}
	});
});






