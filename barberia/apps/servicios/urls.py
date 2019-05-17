from django.urls import path
from . import views 

app_name = "servicios" 

urlpatterns = [
	path('', views.ServiciosListView.as_view(), name="index"),
	path('registrar', views.ServicioCreateView.as_view(), name="registrar"),
	path('<int:pk>/editar', views.ServicioUpdateView.as_view(), name="editar_servicio"),
	path('<int:pk>/eliminar', views.ServicioDeleteView.as_view(), name="eliminar_servicio"),
	path('horarios/', views.HorarioListView.as_view(), name="horario"),
	path('cortes', views.CortesListView.as_view(), name='cortes'),
] 	