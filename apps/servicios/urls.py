
from django.urls import path
from .views import *

app_name = "servicios" 

urlpatterns = [
	path('servicios/', ServiciosList.as_view(), name="servicios"),
	path('horarios/', HorarioList.as_view(), name="horario"),
] 