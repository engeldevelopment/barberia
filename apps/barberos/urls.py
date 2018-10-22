
from django.urls import path
from . import views

app_name = "barberos"

urlpatterns = [
	path('', views.index, name="index"),
	path('barberos/crear', views.BarberoCreateView.as_view(), name='crear'),
	path('barberos/', views.BarberoList.as_view(), name="barberos"),
	path('barberos/<int:pk>', views.BarberoDetail.as_view(), name="detalle-barbero"),
	path('contacto/<int:id_barbero>/crear', views.crear_contacto, name='crear_contacto'),
	path('contacto/<int:pk>/editar', views.ContactoUpdate.as_view(), name='editar_contacto'),
	path('contacto/<int:pk>/eliminar', views.ContactoDelete.as_view(), name='eliminar_contacto'),
]