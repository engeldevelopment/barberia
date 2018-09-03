
from django.urls import path
from .views import *

app_name = "servicios" 

urlpatterns = [
	path('servicios/', ServiciosList.as_view(), name="servicios"),
	path('servicios/crear', ServicioCreate.as_view(), name="crear_servicio"),
	path('servicios/<int:pk>/editar', ServicioUpdate.as_view(), name="editar_servicio"),
	path('servicios/<int:pk>/eliminar', ServicioDelete.as_view(), name="eliminar_servicio"),
	path('horarios/', HorarioList.as_view(), name="horario"),
] 	