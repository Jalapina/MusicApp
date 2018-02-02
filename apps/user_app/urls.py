from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^login/register$', index, name='home'),
    url(r'^register/$', register, name='register'),
    url(r'^auth/$',authentication, name='authentication'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^edit/$', edit, name='edit'),
    url(r'^users/$',users,name='users'),
    url(r'^follow/(?P<followee_id>\d+)$',following,name='followee'),
    url(r'^unfollow/(?P<unfollow_id>\d+)$',unfollow,name='unfollow')
]
