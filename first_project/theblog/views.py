from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView


class HomeView(ListView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        # Your view logic goes here
        context = {'message': 'Blog coming soon!'}
        return render(request, self.template_name, context)


class SlideShowView(ListView):
    template_name = 'slideshow.html'

    def get(self, request, *args, **kwargs):
        # Your view logic goes here
        context = {'message': 'Slideshow coming soon!'}
        return render(request, self.template_name, context)
