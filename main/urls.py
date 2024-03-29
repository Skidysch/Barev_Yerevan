from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from main import settings

urlpatterns = [
    path('', include('places.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
