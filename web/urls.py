
from django.contrib import admin
from django.urls import path, include
from .views import * 

urlpatterns = [
	path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('servicios/', include('apps.servicios.urls')),
    path('barberos/', include('apps.barberos.urls')),
]
