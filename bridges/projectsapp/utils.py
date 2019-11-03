from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from authapp.models import Users
from projectsapp.models import Project


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


class CreateMixin:
    form_model = None
    form = None
    template = None
    variable = None
    viriable_model = None

    def get(self, request, project_pk):
        project = Project.objects.get(pk=project_pk)
        form = self.form(initial={"project": project})
        context = {
            'form': form
        }
        return render(request, template_name=self.template, context=context)

    def post(self, request, project_pk):
        project = Project.objects.get(pk=project_pk)
        form = self.form(request.POST)
        if form.is_valid():
            hacked = {
                "project": Project.objects.get(pk=form.data["project"]),
                self.variable: self.viriable_model.objects.get(pk=form.data[self.variable])
            }
            data = {**form.data, **hacked}
            data = {k: v[0] if isinstance(v, list) else v for k, v in data.items() if
                    k in {f.name for f in self.form_model._meta.fields}}
            data['is_active'] = True if data['is_active'] == 'on' else False
            obj = self.form_model(**data)
            obj.save()
            return HttpResponseRedirect(project.get_absolute_url())
        return HttpResponse(status=400)


class DeleteMixin:
    form_model = None
    template = None

    def get(self, requset, pk):
        obj = get_object_or_404(self.form_model, pk=pk)
        return render(requset, self.template, context={'obj': obj})

    def post(self, request, pk):
        item = get_object_or_404(self.form_model, pk=pk)
        project = item.project
        item.delete()
        return HttpResponseRedirect(project.get_absolute_url())