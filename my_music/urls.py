"""my_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.views import serve

urlpatterns = [
    # url(r'^$', serve,kwargs={'path': 'index.html'}), 
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.playlist_app.urls', namespace='main')),
    url(r'^music/',include('apps.music_app.urls', namespace='music')),
    url(r'^user/', include('apps.user_app.urls', namespace='user')),
    url(r'^api/users/', include("apps.user_app.api.urls", namespace='users-api')),
]
