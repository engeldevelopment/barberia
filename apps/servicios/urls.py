
from django.urls import path
from .views import *

app_name = "servicios" 

urlpatterns = [
	path('servicios/', ServiciosListView.as_view(), name="servicios"),
	path('servicios/crear', ServicioCreateView.as_view(), name="crear_servicio"),
	path('servicios/<int:pk>/editar', ServicioUpdateView.as_view(), name="editar_servicio"),
	path('servicios/<int:pk>/eliminar', ServicioDeleteView.as_view(), name="eliminar_servicio"),
	path('horarios/', HorarioListView.as_view(), name="horario"),
] 	