from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from .models import Post, Categories, Photo
from .forms import PostForm, ImageUploadForm


def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def categoryListView(request):
    cat_menu_list = Categories.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def categoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

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


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        likes_search = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes_search.total_likes()

        liked = False
        if likes_search.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Categories
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class DeletePhotoView(DeleteView):
    model = Photo
    template_name = 'delete_photo.html'
    success_url = reverse_lazy('gallery')

