
from django.urls import path
from .views import *

app_name = "barberos"

urlpatterns = [
	path('', index, name="index"),
	path('barberos/', BarberoList.as_view(), name="barberos"),
	path('barberos/<int:id_barbero>/', informacion_de_barbero, name="info"),
	path('contacto/<int:pk>/editar', ContactoUpdate.as_view(), name='editar_contacto'),
	path('contacto/<int:pk>/eliminar', ContactoDelete.as_view(), name='eliminar_contacto'),
]