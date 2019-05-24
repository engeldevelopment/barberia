$(() => {

	var csrfToken = $.cookie('csrftoken'); 

	$.ajaxSetup({
		beforeSend: (xhr, settings) => {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader('X-CSRFToken', csrfToken);
			}
		}
	});

});

function csrfSafeMethod(method) {
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}