from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from .models import Photo
from .forms import ImageUploadForm





class HomeView(ListView):
    model = Photo
    template_name = 'gallery.html'
    ordering = ['-post_date']



def galleryView(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render (request, 'gallery.html', context)

def photoView(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo':photo})


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
