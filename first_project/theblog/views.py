from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post, Categories
from .forms import PostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
def CategoryListView(request):
    cat_menu_list = Categories.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.title().replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '),
        'category_posts':category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categories.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
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