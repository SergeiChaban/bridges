from django.urls import path


app_name = 'projectsapp'

urlpatterns = [
    path('', ProjectsList.as_view(), name='projects'),

