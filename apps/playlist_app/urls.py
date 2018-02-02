from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/edit/$',profile_edit, name='profile_edit' ),
    url(r'^playlist$', playlist, name='playlist'),
    url(r'^playlist/remove(?P<playlist_id>\d+)$', remove_playlist, name='remove')
]

