from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . views import HomeView, galleryView, photoView, ImageUploadView, DeletePhotoView, SlideshowView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('photo/<str:pk>/delete', DeletePhotoView.as_view(), name='delete_photo'),
    path('gallery/', galleryView, name='gallery'),
    path('slideshow/', SlideshowView.as_view(), name='slideshow'),
    path('photo/<str:pk>/', photoView, name='photo'),
    path('post_photos/', ImageUploadView.as_view(), name='post_photos'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
