




class ProjectsList(ListView):

    model = Project


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        values = ProjectHasTechnicalSolutions.objects.all()

                        'page_title': 'Проекты компании',
                        'bred_title': 'Проекты компании'
                        })
        return context















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
