from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('user_auth/', include('django.contrib.auth.urls')),
    path('user_auth/', include('user_auth.urls')),
    path('photo_gallery/', include('photo_gallery.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
