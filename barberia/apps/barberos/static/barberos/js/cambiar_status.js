$('#cambiar-status').click((e) => {
	e.preventDefault();

	$.post($("#form-cambiar-status").attr('action'), 
		function(data, textStatus, xhr) {

		addClassAStatus(data.status, data.pk);
		alert(`Haz cambiado tu estado a ${getStatus(data.status)}`);
		console.log(data);
	});
});


function getStatus(status) {
	return (status? "Activo" : "Inactivo");
}

function addClassAStatus(status, pk) {
	var clase = (status? "fas fa-toggle-on" : "fas fa-toggle-off");
	$(`#status-${pk}`).addClass(clase);
}