
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import RegistrarServicio


class ServicioCreate(generic.CreateView):
	model = Servicio
	form_class = RegistrarServicio
	template_name = 'servicios/registrar_servicio.html'
	success_url = reverse_lazy('servicios:servicios') 	


class ServiciosList(generic.ListView):
	model = Servicio
	context_object_name = "servicios"
	template_name = "servicios/listar_servicios.html"
	queryset = Servicio.objects.all().order_by('-precio')


class ServicioUpdate(generic.UpdateView):
	model = Servicio
	form_class = RegistrarServicio
	template_name = 'servicios/editar_servicio.html'
	context_object_name = 'servicio'
	success_url = reverse_lazy('servicios:servicios')


class ServicioDelete(generic.DeleteView):
	model = Servicio
	template_name = 'servicios/eliminar_servicio.html'
	context_object_name = 'servicio'
	success_url = reverse_lazy('servicios:servicios') 		


class HorarioList(generic.ListView):
	model = Horario
	context_object_name = "horarios"
	template_name = "servicios/listar_horarios.html"