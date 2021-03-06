from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import *
from .forms import ServicioForm


class ServicioCreateView(LoginRequiredMixin,
						PermissionRequiredMixin, 
						generic.CreateView):
	model = Servicio
	form_class = ServicioForm
	permission_required = ('servicios.add_servicio',)
	template_name = 'servicios/servicio_form.html'
	success_url = reverse_lazy('servicios:index') 	


class ServiciosListView(generic.ListView):
	model = Servicio
	context_object_name = "servicios"
	template_name = "servicios/listar_servicios.html"
	queryset = Servicio.objects.all().order_by('-precio')


class ServicioUpdateView(LoginRequiredMixin,
						PermissionRequiredMixin,
						generic.UpdateView):
	model = Servicio
	form_class = ServicioForm
	permission_required = ('servicios.edit_servicio',)
	template_name = 'servicios/servicio_form.html'
	context_object_name = 'servicio'
	success_url = reverse_lazy('servicios:index')


class ServicioDeleteView(LoginRequiredMixin,
						PermissionRequiredMixin,
						generic.DeleteView):
	model = Servicio
	template_name = 'servicios/eliminar_servicio.html'
	context_object_name = 'servicio'
	success_url = reverse_lazy('servicios:index') 		
	permission_required = ('servicios.delete_servicio')

class HorarioListView(generic.ListView):
	model = Horario
	context_object_name = "horarios"
	template_name = "servicios/listar_horarios.html"


class CortesListView(generic.ListView):
	model = Corte
	template_name = 'servicios/listar_cortes.html'
	context_object_name = 'cortes'	