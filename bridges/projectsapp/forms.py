from django import forms
from django.core.exceptions import ValidationError
from authapp.models import Users
from productsapp.models import TechnicalSolutions
from .models import *

from django.utils.safestring import mark_safe


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'status', 'city', 'address', 'coordinate', 'description', 'is_active']


class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManagers
        fields = ['manager', 'role', 'project']

class ProjectSolutionsForm(forms.ModelForm):
    class Meta:
        model = ProjectHasTechnicalSolutions



class ProjectCompanyForm(forms.ModelForm):
    class Meta:
        model = ProjectCompany
        fields = ['company', 'role']


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']

