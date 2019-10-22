from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from authapp.models import Users
from projectsapp.forms import ProjectManagerCreateForm
from projectsapp.models import Project, ProjectManagers


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('projectsapp:projects')
        return render(request, self.template, context={'form': bound_form})

