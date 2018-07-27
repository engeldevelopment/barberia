
$(document).ready(function() {
	
	$('nav a').click(function(event) {
		e.preventDefault();

		$.ajax({
			url: $(this).attr('href'),
			data: $(this).serialize(),
		})
		.done(function(datos) {
			$('body').html(""+datos);
			console.log("success");
		})
		.fail(function() {
			console.log("error");
		});
	});
});