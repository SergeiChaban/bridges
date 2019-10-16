from django.shortcuts import render


def partners_list(request):
    return render(request, 'partnersapp/partners_list.html')
