from django import forms
from .models import Service, ServiceCategory
from django.core.exceptions import ValidationError


class ServiceForm(forms.Form):
    # category = forms.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = forms.CharField(label = 'Наименование услуги', max_length=128)
    slug = forms.CharField(label = 'Заполняется автоматически', max_length=128, required=False)
    description = forms.CharField(label = 'Поле для описания услуги', max_length=500)
    image = forms.FileField()


    name.widget.attrs.update({'class':'form-control'})
    slug.widget.attrs.update({'class':'form-control'})
    description.widget.attrs.update({'class':'form-control'})
    image.widget.attrs.update({'class':'form-control-file'})

    def clean_slug(self):
        new_service = self.cleaned_data['slug'].lower()

        if new_service == 'create':
            raise ValidationError('Slug may not be "Create"')
            return new_service


    def save(self):
        new_service = Service.objects.create(
            name = self.cleaned_data['name'],
            slug = self.cleaned_data['slug'],
            description = self.cleaned_data['description'],
            image = self.cleaned_data['image'],
            )
        return new_service