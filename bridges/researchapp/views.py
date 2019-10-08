from django.shortcuts import render

from authapp.models import Companies
from researchapp.models import Document


def research(request):
    companies = Document.objects.order_by('company').distinct('company__name_company').values('company__name_company',
                                                                                              'file__file', 'pk',
                                                                                              'name', 'type_id',
                                                                                              'description')
    # documents = Document.objects.filter(author__in=[1,]).exclude(type__id=2)
    documents = Document.objects.all().values('company__name_company', 'file__file', 'pk', 'name', 'type_id',
                                              'description')

    content = {
        'companies': companies,
        'documents': documents
    }

    return render(request, 'researchapp/research.html', content)
