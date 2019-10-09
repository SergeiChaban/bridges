from django.shortcuts import render

from authapp.models import Companies
from researchapp.models import Document


def research(request):
    documents = Document.objects.filter(type_id__in=(2, 3,)).order_by('-company').values('company__name_company',
                                                                                         'file__file', 'pk', 'name',
                                                                                         'type_id', 'description')
    companies = documents.distinct('company__name_company')

    content = {
        'companies': companies,
        'documents': documents
    }

    return render(request, 'researchapp/research.html', content)
