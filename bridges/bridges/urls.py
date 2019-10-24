from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('contact/', include('contactapp.urls', namespace='contact')),
    path('products/', include('productsapp.urls', namespace='products')),
    path('projects/', include('projectsapp.urls', namespace='projects')),
    path('services/', include('servicesapp.urls', namespace='services')),
    path('map/', include('ymapapp.urls', namespace='ymap')),
    path('admin/', admin.site.urls),
    path('research/', include('researchapp.urls', namespace='research')),
    path('auth/', include('authapp.urls', namespace='auth'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
