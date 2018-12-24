
from django.urls import path
from . import views 

app_name = "servicios" 

urlpatterns = [
	path('servicios/', views.ServiciosList.as_view(), name="servicios"),
	path('servicios/crear', views.ServicioCreate.as_view(), name="crear_servicio"),
	path('servicios/<int:pk>/editar', views.ServicioUpdate.as_view(), name="editar_servicio"),
	path('servicios/<int:pk>/eliminar', views.ServicioDelete.as_view(), name="eliminar_servicio"),
	path('horarios/', views.HorarioList.as_view(), name="horario"),
	path('cortes', views.CortesListView.as_view(), name='cortes'),
] 	