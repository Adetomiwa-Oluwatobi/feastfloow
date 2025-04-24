"""
URL configuration for feastflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project_root/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='users/register/', permanent=False)),
    path('users/', include('apps.users.urls',namespace='users')),
    path('posts/', include('apps.posts.urls', namespace='posts')),
    path('followers/', include('apps.followers.urls', namespace='followers')),
    path('teams/', include('apps.teams.urls', namespace='teams')),
    path('search/', include('apps.searchandfilters.urls', namespace='searchandfilters')),
    path('ratings/', include('apps.ratingsandreviews.urls', namespace='ratingsandreviews')),
    path('event/', include('apps.event.urls', namespace='event')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)