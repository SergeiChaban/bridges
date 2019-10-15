from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from productsapp.models import TechnicalSolutions
from projectsapp.forms import ProjectSolutionsForm, ProjectManagerForm, ProjectCompanyForm, ProjectForm
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions, ProjectCompany, ProjectManagers
# Create your views here.
from projectsapp.utils import ObjectCreateMixin


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











def company_update(request, pk):
    if id:
        project = Project.objects.get(pk=pk)
    else:
        project = Project()
    project_form = ProjectForm(instance=project)
    BookInlineFormSet = inlineformset_factory(Project, ProjectCompany, form=ProjectCompanyForm, extra=1)
    formset = BookInlineFormSet(instance=project)
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if id:
            project_form = ProjectForm(request.POST, instance=project)
            formset = BookInlineFormSet(request.POST)
            if project_form.is_valid():
                created_project = project_form.save(commit=False)
                formset = BookInlineFormSet(request.POST, instance=created_project)
                if formset.is_valid():
                    created_project.save()
                    formset.save()
                    return HttpResponseRedirect(created_project.get_absolute_url())
    context ={
        "project_form": project_form,
        "formset": formset,
        'page_title': 'Добавление контрагентов',
    }
    return render(request, "projectsapp/company_update.html", context)
