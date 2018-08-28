
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import * 
from .forms import RegistrarContacto


class BarberoList(generic.ListView):
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


def index(request):
	return render(request, 'barberos/index.html')


class ContactoUpdate(generic.UpdateView):
	model = Contacto
	form_class = RegistrarContacto
	template_name = 'barberos/add_contacto.html'
	context_object_name = 'contacto'
	success_url = reverse_lazy('barberos:barberos')


class ContactoDelete(generic.DeleteView):
	model = Contacto
	template_name = 'barberos/eliminar_contacto.html'
	context_object_name = 'contacto'
	success_url = reverse_lazy('barberos:barberos')	