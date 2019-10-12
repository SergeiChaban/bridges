from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, CreateView, DeleteView

from django.http import HttpResponseRedirect
from django.db.models import Q

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project, ProjectImage, ProjectHasTechnicalSolutions


# Create your views here.
class ProjectsList(ListView):

    model = Project
    pk_field = 'techsol'
    paginate_by = 6    
    template_name = 'projectsapp/grid.html'   

    def get_queryset(self, **kwargs):
        query = Q()
        if 'pk' in self.kwargs:
            query = Q((self.pk_field, self.kwargs['pk']))
            return super().get_queryset().filter(query)
        else:
            return super().get_queryset() 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        values = ProjectHasTechnicalSolutions.objects.all()
        context.update({'values': values,
                        'page_title': 'Проекты компании',
                        'bred_title': 'Проекты компании'
                        })
        return context



def project(request, pk):
    title = 'Проекты компании'
    item = get_object_or_404(Project, pk=pk)
    gallery = ProjectImage.objects.filter(project__pk=pk)
    values = ProjectHasTechnicalSolutions.objects.filter(project__pk=pk)

    content = {
        'page_title': title,
        'bred_title': title,
        'project': item,
        'gallery': gallery,
        'values': values
    }
    return render(request, 'projectsapp/project.html', content)

