from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DeleteView, DetailView

from django.http import HttpResponseRedirect
from django.db.models import Q

from productsapp.models import TechnicalSolutions
from projectsapp.forms import ProjectSolutionsForm
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions


# Create your views here.
class ProjectsList(ListView):

    model = Project


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        values = ProjectHasTechnicalSolutions.objects.all()
        context.update({'values': values,
                        'page_title': 'Проекты компании',
                        'bred_title': 'Проекты компании'
                        })
        return context





