from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout
from links.urls import urlpatterns as linksPatterns
from django.conf.urls import include
from links import urls as linksUrls
from links.views import RedirectToDestination

from config.api import api



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    path('api/links/', include(linksUrls)),
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
