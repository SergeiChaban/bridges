from django import forms
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
        fields = ['techsol', 'name', 'value']


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']


class ProjectManagerCreateForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProjectManagers
        fields = '__all__'


class ProjectCompanyCreateForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProjectCompany
        fields = '__all__'


class ProjectSolutionsCreateForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProjectHasTechnicalSolutions
        fields = '__all__'


class ProjectDiscussItemForm(forms.ModelForm):
    class Meta:
        model = ProjectDiscussItem
        fields = ['comment']


class ProjectDiscussMemberForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image']


class ProjectManagerUpdateFormset(forms.models.BaseInlineFormSet):
    management_template = '<{tag} name="{prefix}-management_form">{form}</{tag}>'.format
    form_template = '<{tag} name="{prefix}-{index}-form">{form}</{tag}>'.format
    default_render = 'as_ul'

    def add_fields(self, form, index):
        super(ProjectManagerUpdateFormset, self).add_fields(form, index)
        form.fields['DELETE'].widget.attrs['onchange'] = 'rowhidder(this);'

    def render(self, **kwargs):
        forms = [self.render_management()]
        forms += [self.render_form(index, form, **kwargs) for index, form in enumerate(self)]
        return mark_safe(''.join(forms))

    def render_form(self, index, form, **kwargs):
        tag = kwargs.setdefault('tag', 'table')
        method = kwargs.setdefault('method', f'as_{tag}')
        return self.form_template(index=index, form=getattr(form, method)(), prefix=self.prefix, **kwargs)

    def as_table(self):
        "Returns this formset rendered as HTML <table></table>s."
        return self.render(tag='table')

    def as_p(self):
        "Returns this formset rendered as HTML <div></div>s."
        return self.render(tag='div', method='as_p')

    def as_ul(self):
        "Returns this formset rendered as HTML <ul></ul>s."
        return self.render(tag='ul')

    def __str__(self):
        "Returns this formset rendered as self.default_render"
        return getattr(self, self.default_render, self.as_table)()

    def render_management(self):
        return mark_safe(self.management_template(tag='fieldset', prefix=self.prefix, form=str(self.management_form)))