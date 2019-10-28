from django.urls import path
from .views import NewsListView
from .views import NewsDetailView
from .views import NewsCreateView
from .views import NewsDeleteView
from .views import NewsUpdateView

app_name = 'newsapp'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('update/<int:pk>', NewsUpdateView.as_view(), name='news_supdate'),
    path('create/<int:project_pk>', NewsCreateView.as_view(), name='news_create'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
]
