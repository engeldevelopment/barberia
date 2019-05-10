
$(document).ready(function() {
	
	$('nav a').click(function(e) {
		e.preventDefault();
		
		$.get($(this).attr('href'), 
			function(data) {
			$('body').html(data)
		});
	});
});