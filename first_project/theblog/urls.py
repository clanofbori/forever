from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . views import HomeView, SlideShowView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('slideshow/', SlideShowView.as_view(), name='index.html'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
