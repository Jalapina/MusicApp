from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'), #music home page
    url(r'^adding$',music, name='add'), #logic for adding Artist and Albums
    url(r'^add/song/(?P<album_id>\d+)$',adding_song, name='song'), #logic for adding songs
    url(r'^add_artist/(?P<artist_id>\d+)$', add_artist, name='extra_add'),
    url(r'^album/(?P<album_id>\d+)$',album, name='albums'),#renders album for a specfic artsit
    url(r'^fan/(?P<artist_id>\d+)$',fans, name='fans')
]
