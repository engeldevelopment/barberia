
from django.urls import path
from . import views

app_name = "barberos"

urlpatterns = [
	path('', views.BarberoList.as_view(), name="barberos"),
	path('registrar/', views.BarberoCreateView.as_view(), name='registrar'),
	path('<int:pk>/detalle', views.BarberoDetail.as_view(), name="detalle"),
	path('<int:pk>/eliminar', views.BarberoDeleteView.as_view(), name="eliminar"),
	path('contacto/<int:id_barbero>/crear', views.crear_contacto, name='crear_contacto'),
	path('contacto/<int:pk>/editar', views.ContactoUpdate.as_view(), name='editar_contacto'),
	path('contacto/<int:pk>/eliminar', views.ContactoDelete.as_view(), name='eliminar_contacto'),
]