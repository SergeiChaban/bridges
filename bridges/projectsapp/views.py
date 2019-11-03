from django.contrib.auth.decorators import user_passes_test
from django.forms import inlineformset_factory, modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from projectsapp.utils import CreateMixin, DeleteMixin
from .forms import *
from projectsapp.models import ProjectImage, ProjectManagers
from django.views.generic import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from projectsapp.models import Project, ProjectHasTechnicalSolutions, ProjectCompany
from authapp.models import Users

from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy


class ProjectsList(ListView):
    """docstring for ProductList"""
    paginate_by = 6
    model = Project
    template_name = 'projectsapp/grid.html'
    extra_context = {}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all()
        else:
            return Project.objects.filter(status__exact='завершен')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = TechnicalSolutions.objects.all()
        values = ProjectHasTechnicalSolutions.objects.all()
        context.update({'products': products,
                        'values': values,
                        'page_title': 'Проекты компании',
                        'bred_title': 'Проекты компании'
                        })
        return context


class ProjectRead(DetailView):
    model = Project
    extra_context = {}    
    not_empty_url = reverse_lazy('projects:project')

    def get_queryset(self):
        if self.request.user.is_staff:
            return Project.objects.all()
        else:
            return Project.objects.filter(status__exact='завершен')

    def get_context_data(self, **kwargs):
        context = super(ProjectRead, self).get_context_data(**kwargs)
        context.update({'page_title': 'Детальная информация о проекте',
                        'bred_title': 'Информация о проекте'
                        })
        return context


#  ------------------------------------ PROJECT'S DETAILS ----------------------------------------------


@user_passes_test(lambda u: u.is_superuser)
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_form = ProjectUpdateForm(instance=project)
    if request.method == 'POST':
        project_form = ProjectUpdateForm(request.POST, instance=project)
        if project_form.is_valid():
            project_form.save()
            return HttpResponseRedirect(project.get_absolute_url())
    context = {
        'project_form': project_form,
        'page_title': 'Редактирование основной информации',
        'bred_title': 'Обновление проекта',
        'project': project
    }
    return render(request, 'projectsapp/company_update.html', context)


#  ------------------------------------ PROJECT'S SOLUTIONS ----------------------------------------------


class ProjectsSolutionsCreateView(CreateMixin, View):
    form_model = ProjectHasTechnicalSolutions
    form = ProjectSolutionsCreateForm
    template = 'projectsapp/projectsolutions_form.html'
    FormSet = modelformset_factory(form_model, fields='__all__')
    variable = 'techsol'
    viriable_model = TechnicalSolutions


class ProjectsSolutionsDeleteView(DeleteMixin, View):
    form_model = ProjectHasTechnicalSolutions
    template = 'projectsapp/projectmanagers_confirm_delete.html'


# def company_update(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     project_form = ProjectForm(instance=project)
#     company_formset = inlineformset_factory(Project, ProjectCompany, form=ProjectCompanyForm, extra=1)
#     formset = company_formset(instance=project)
#     if request.method == "POST":
#         project_form = ProjectForm(request.POST)
#         project_form = ProjectForm(request.POST, instance=project)
#         formset = company_formset(request.POST)
#         if project_form.is_valid():
#             created_project = project_form.save(commit=False)
#             formset = company_formset(request.POST, instance=created_project)
#             if formset.is_valid():
#                 created_project.save()
#                 formset.save()
#                 return HttpResponseRedirect(created_project.get_absolute_url())
#     context ={
#         'project_form': project_form,
#         'formset1': formset,
#         'page_title': 'Добавление контрагентов',
#         'bred_title': 'Добавление контрагентов',
#         'project': project
#     }
#     return render(request, "projectsapp/company_update.html", context)

#  ------------------------------------ PROJECT'S MANAGERS CRUD ----------------------------------------------
    
# class CreateProjectManager(PermissionRequiredMixin, CreateView):
#     model = ProjectManagers
#     form_class = ProjectManagerCreateForm
#     permission_required = f'{model._meta.app_label}.change_{model.__name__}'
#     template = 'projectsapp/projectmanagers_form.html'
#
#
#
#     form = ProjectManagerCreateForm
#     def get(self, request, project_pk):
#         self.project = Project.objects.get(pk=project_pk)
#         self.success_url = self.project.get_absolute_url()
#         form = self.form(initial={"project": self.project})
#         context = {
#             'form': form
#         }
#         return render(request, template_name=self.template, context=context)
#
#     def form_valid(self, form, **kwargs):
#         response = super().form_valid(form)
#         if form(**kwargs).is_valid():
#             form.save()
#         return reverse(self.success_url)
#
#     def get_context_data(self, **kwargs):
#         project = Project.objects.get(pk=project_pk)
#         context = super(CreateProjectManager, self).get_context_data(**kwargs)
#         context.update({"project": project})
#         return context
#
# class DeleteProjectManager(PermissionRequiredMixin, DeleteView):
#     model = ProjectManagers
#     permission_required = f'{model._meta.app_label}.change_{model.__name__}'
#
#     template = 'projectsapp/projectmanagers_confirm_delete.html'
#
#     def post(self, request, pk):
#         item = get_object_or_404(self.model, pk=pk)
#         project = item.project
#         item.delete()
#         return HttpResponseRedirect(project.get_absolute_url())


# #  ------------------------------------ UPDATE PROJECT'S MANAGERS ----------------------------------------------
# class ProductManagersUpdate(PermissionRequiredMixin, UpdateView):
#     model = Project
#     form_class = ProjectManagerForm
#     permission_required = f'{model._meta.app_label}.change_{model.__name__}'
#     template_name = 'projectsapp/company_update.html'
#     request = None

#     def get_formset_class(self, formset=ProjectManagerUpdateFormset, extra=1, form=ProjectManagerForm, fk_name='project', **kwargs):
#         return inlineformset_factory(
#             self.model, ProjectManagerForm._meta.model, formset=formset, extra=extra, form=form, fk_name=fk_name)

#     def get_formset(self, **kwargs):
#         self.formset = self.get_formset_class(**kwargs)(
#             data=self.request and self.request.POST or None,
#             files=self.request and self.request.FILES or None,
#             instance=getattr(self, 'object', self.get_object()), initial=kwargs.get('initial', {}))
#         print("fomset: ", self.formset)
#         return self.formset

#     def form_valid(self, form, **kwargs):
#         response = super().form_valid(form)
#         if self.get_formset(**kwargs).is_valid():
#             self.formset.save()
#         print("===============================")
#         print("responce: ", response)
#         print("===============================")
#         return response

#     def get_context_data(self, **kwargs):
#         print("===============================")
#         print("context: ", super().get_context_data(formset1=self.get_formset(), **kwargs))
#         print("===============================")
#         return super().get_context_data(formset1=self.get_formset(), **kwargs)

# def project_managers_update(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     project_form = ProjectForm(instance=project)
#     managers_formset = inlineformset_factory(Project, ProjectManagers, form=ProjectManagerForm, extra=1)
#     formset = managers_formset(instance=project)
#     if request.method == 'POST':
#         project_form = ProjectForm(request.POST, instance=project)
#         formset = managers_formset(request.POST)
#         if project_form.is_valid():
#             updated_project = project_form.save(commit=False)
#             formset = managers_formset(request.POST, instance=updated_project)
#             if formset.is_valid():
#                 updated_project.save()
#                 formset.save()
#                 return HttpResponseRedirect(updated_project.get_absolute_url())
#     context = {
#         'project_form': project_form,
#         'formset': formset,
#         'page_title': 'Обновление списка участников',
#         'bred_title': 'Список участников',
#         'project': project
#     }
#     return render(request, 'projectsapp/company_update.html', context)

#  ------------------------------------ PROJECT'S COMPANIES ----------------------------------------------


class ProjectsCompanyCreateView(CreateMixin, View):
    form_model = ProjectCompany
    form = ProjectCompanyCreateForm
    template = 'projectsapp/projectcompany_form.html'
    FormSet = modelformset_factory(form_model, fields='__all__')
    variable = 'company'
    viriable_model = Company


class ProjectsCompanyDeleteView(DeleteMixin, View):
    form_model = ProjectCompany
    template = 'projectsapp/projectmanagers_confirm_delete.html'


#  ------------------------------------ PROJECT'S MANAGERS ----------------------------------------------

class ProjectsManagerCreateView(CreateMixin, View):
    form_model = ProjectManagers
    form = ProjectManagerCreateForm
    template = 'projectsapp/projectmanagers_form.html'
    FormSet = modelformset_factory(form_model, fields='__all__')
    variable = 'manager'
    viriable_model = Users


class ProjectsManagerDeleteView(DeleteMixin, View):
    form_model = ProjectManagers
    template = 'projectsapp/projectmanagers_confirm_delete.html'


#  ------------------------------------ PROJECT'S GALLERY ----------------------------------------------


@user_passes_test(lambda u: u.is_superuser)
def gallery_update(request, pk):
    project = Project.objects.get(pk=pk)
    project_form = ProjectForm(instance=project)
    BookInlineFormSet = inlineformset_factory(Project, ProjectImage, form=ProjectImageForm, extra=3)
    formset = BookInlineFormSet(instance=project)
    if request.method == "POST":
        project_form = ProjectForm(request.POST, instance=project)
        formset = BookInlineFormSet(request.POST, request.FILES)
        if project_form.is_valid():
            created_project = project_form.save(commit=False)
            formset = BookInlineFormSet(request.POST, request.FILES, instance=created_project)
            if formset.is_valid():
                created_project.save()
                formset.save()
                return HttpResponseRedirect(created_project.get_absolute_url())
    context = {
        'project_form': project_form,
        'formset': formset,
        'page_title': 'Добавление фотографий',
        'bred_title': 'Добавление фотографий',
        'project': project
    }
    return render(request, "projectsapp/gallery_update.html", context)


def project_discuss_items(request, pk):
    project = Project.objects.get(pk=pk)
    project_discuss_items = ProjectDiscussItem.objects.filter(project_id=pk)
    discuss_users = ProjectDiscussMember.objects.filter(project_id=pk)
    self_user = request.user
    if discuss_users.filter(user=self_user).exists():
        if request.method == 'POST':
            report_form = ProjectDiscussItemForm(data=request.POST)
            if report_form.is_valid():
                new_report_form = report_form.save(commit=False)
                new_report_form.project = project
                new_report_form.user = request.user
                new_report_form.save()
                return redirect(project.get_absolute_discuss_url())
        else:
            report_form = ProjectDiscussItemForm()
        context = {
            'object': project,
            'project_discuss_items': project_discuss_items,
            'discuss_users': discuss_users,
            'form': report_form,
            'page_title': 'Обсуждение проекта',
            'bred_title': 'Обсуждение проекта',
        }
        return render(request, 'projectsapp/project_discuss_detail.html', context)
    else:
        context = {
            'page_title': 'Доступ запрещен',
        }
        return render(request, 'projectsapp/project_access_denied.html', context)


def project_discuss_edit_members(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_form = ProjectForm(instance=project)
    InlineFormset = inlineformset_factory(Project, ProjectDiscussMember, form=ProjectDiscussMemberForm, extra=1)
    formset = InlineFormset(instance=project)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST, instance=project)
        formset = InlineFormset(request.POST)
        if project_form.is_valid():
            updated_project_form = project_form.save(commit=False)
            formset = InlineFormset(request.POST, instance=updated_project_form)
            if formset.is_valid():
                updated_project_form.save()
                formset.save()
                return HttpResponseRedirect(project.get_absolute_discuss_url())
    context = {
        'project': project,
        'form': project_form,
        'formset': formset,
        'page_title': 'Редактирование участников проекта',
        'bred_title': 'Редактирование участников проекта',
    }
    return render(request, 'projectsapp/discuss_members_update.html', context)