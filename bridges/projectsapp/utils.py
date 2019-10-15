from django.shortcuts import render, redirect
from django.urls import reverse


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


class ObjectDeleteMixin:
    model = None
    template = None
    context = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        return render(request, self.template, context={self.context: obj})

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        obj.delete()
        return redirect(reverse('projectsapp:projects'))
