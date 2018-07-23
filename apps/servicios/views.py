
from django.shortcuts import render
from django.views.generic import *
from .models import *


class ServiciosList(ListView):
	model = Servicio
	context_object_name = "servicios"
	template_name = "servicios/listar_servicios.html"
	queryset = Servicio.objects.all().order_by('-precio')


class HorarioList(ListView):
	model = Horario
	context_object_name = "horarios"
	template_name = "servicios/listar_horarios.html"