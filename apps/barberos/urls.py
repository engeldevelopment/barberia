
from django.urls import path
from .views import *

app_name = "barberos"

urlpatterns = [
	path('barberos/', BarberoList.as_view(), name="barberos"),
	path('barberos/<int:id_barbero>/', informacion_de_barbero, name="info"),
]