from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . views import HomeView, ArticleDetailView, AddPostView, UpdatePostView,\
DeletePostView, AddCategoryView, categoryView, categoryListView, likeView,\
galleryView, photoView, ImageUploadView, DeletePhotoView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('photo/<str:pk>/delete', DeletePhotoView.as_view(), name='delete_photo'),
    path('categories/<str:cats>/', categoryView, name='category'),
    path('category-list/', categoryListView, name='category-list'),
    path('like/<int:pk>', likeView, name='like_post'),
    path('gallery/', galleryView, name='gallery'),
    path('photo/<str:pk>/', photoView, name='photo'),
    path('post_photos/', ImageUploadView.as_view(), name='post_photos'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
