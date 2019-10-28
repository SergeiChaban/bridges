from django.shortcuts import render

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from django.contrib.auth.mixins import  PermissionRequiredMixin

from .models import News, NewsImage

# Create your views here.
class NewsListView(ListView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}

# Create your views here.
class NewsDetailView(DetailView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}


# Create your views here.
class NewsCreateView(PermissionRequiredMixin, CreateView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}


# Create your views here.
class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}




# Create your views here.
class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}


