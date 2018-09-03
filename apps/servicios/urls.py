
from django.urls import path
from .views import *

app_name = "servicios" 

urlpatterns = [
	path('servicios/', ServiciosList.as_view(), name="index"),
	path('crear/', ServicioCreate.as_view(), name='crear_servicio'),
	path('servicios/<int:pk>/editar/', ServicioUpdate.as_view(), name="editar_servicio"),
	path('horarios/', HorarioList.as_view(), name="horario"),
] 	