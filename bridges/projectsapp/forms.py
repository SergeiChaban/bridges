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



class ProjectSolutionsForm(forms.ModelForm):
    class Meta:
        model = ProjectHasTechnicalSolutions



class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']



