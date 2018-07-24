
from django.shortcuts import render
from django.views.generic import * 
from .models import * 


class BarberoList(ListView):
	model = Barbero
	context_object_name = "barberos"
	template_name = "barberos/listar_barberos.html"



def informacion_de_barbero(request, id_barbero):
	barbero = Barbero.objects.get(pk=id_barbero)
	contactos = Contacto.objects.filter(barbero=barbero)
	cuentas = Cuenta.objects.filter(barbero=barbero)

	return render(request, "barberos/detalle_barbero.html",\
		{'barbero': barbero,
		 'contactos': contactos,
		 'cuentas': cuentas
		})	
