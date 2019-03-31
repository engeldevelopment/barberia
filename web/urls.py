
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', include('apps.home.urls')),
    path('admin/', admin.site.urls),
    path('servicios/', include('apps.servicios.urls')),
    path('barberos/', include('apps.barberos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)