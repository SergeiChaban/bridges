# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from django.contrib.auth.mixins import  PermissionRequiredMixin

from .models import News


# Create your views here.
class NewsListView(ListView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({})
        print(context)
        print(context['object_list'][0].__dict__.items())
        return context

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


