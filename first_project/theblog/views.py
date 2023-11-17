from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, FormView
from .models import Photo
from .forms import ImageUploadForm
from .constants import VALID_IMAGE_EXTENSIONS, VALID_VIDEO_EXTENSIONS


class HomeView(ListView):
    model = Photo
    template_name = 'home.html'
    ordering = ['-post_date']

def galleryView(request):
    photos = Photo.objects.all()
    return render (request, 'gallery.html', {
                    'photos': photos,
                   'valid_image_extensions': VALID_IMAGE_EXTENSIONS,
                   'valid_video_extensions': VALID_VIDEO_EXTENSIONS,
                   })

def photoView(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {
                    'photo':photo,
                    'valid_image_extensions': VALID_IMAGE_EXTENSIONS,
                    'valid_video_extensions': VALID_VIDEO_EXTENSIONS,
                    })


class SlideshowView(HomeView):
    template_name = 'slideshow.html'


class ImageUploadView(FormView):
    template_name = 'post_photos.html'
    form_class = ImageUploadForm
    success_url = reverse_lazy('gallery')

    def form_valid(self, form):
        for image in self.request.FILES.getlist('image'):
            Photo.objects.create(image=image)
        return super().form_valid(form)


class DeletePhotoView(DeleteView):
    model = Photo
    template_name = 'delete_photo.html'
    success_url = reverse_lazy('gallery')
