from django import forms
from django.core.exceptions import ValidationError
from authapp.models import Users
from productsapp.models import TechnicalSolutions
from projectsapp.models import Project, ProjectHasTechnicalSolutions, ProjectManagers


class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManagers
        fields = ['role', 'manager', 'project']


class ProjectSolutionsForm(forms.ModelForm):
    class Meta:
        model = ProjectHasTechnicalSolutions
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(ProjectSolutionsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
