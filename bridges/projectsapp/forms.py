from django import forms

from productsapp.models import TechnicalSolutions
from projectsapp.models import Project, ProjectHasTechnicalSolutions


# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         exclude = ('name', 'slug', 'city', 'coordinates', 'descriptions', 'image', 'status', 'address', 'map_mark', 'text_for_map')
#
#     def __init__(self, *args, **kwargs):
#         super(ProjectForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'


# class ProjectSolutions(forms.Form):
#     name = forms.CharField(label='название', max_length=100)
#     techsol = forms.ModelChoiceField(queryset=TechnicalSolutions.objects.all())
#     project = forms.ModelChoiceField(queryset=Project.objects.all())
#     value = forms.DecimalField(verbose_name='ОБъем работ', max_digits=18, decimal_places=2, null=True)


class ProjectSolutionsForm(forms.ModelForm):
    class Meta:
        model = ProjectHasTechnicalSolutions
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(ProjectSolutionsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class RegisterUserForm(ModelForm):
#     class Meta:
#         model = Users
#         fields = ('username', 'password', 'phone')
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Введите логин*'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'придумайте пароль*'}),
#             'phone': forms.TextInput(attrs={'placeholder': 'и укажите телефон для связи*', }),
#         }
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         user.is_active = False
#         if commit:
#             user.save()
#         return user
