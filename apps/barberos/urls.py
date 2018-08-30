
from django.urls import path
from .views import *

app_name = "barberos"

urlpatterns = [
	path('', index, name="index"),
	path('barberos/', BarberoList.as_view(), name="barberos"),
	path('barberos/<int:pk>', BarberoDetail.as_view(), name="detalle-barbero"),
	path('contacto/<int:id_barbero>/crear', crear_contacto, name='crear_contacto'),
	path('contacto/<int:pk>/editar', ContactoUpdate.as_view(), name='editar_contacto'),
	path('contacto/<int:pk>/eliminar', ContactoDelete.as_view(), name='eliminar_contacto'),
]