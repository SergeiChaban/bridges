from django.shortcuts import render

from researchapp.models import Document


def research(request):
    documents = Document.objects.all()
    content = {
        'documents': documents,
    }
    return render(request, 'researchapp/research.html', content)
