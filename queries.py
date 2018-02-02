import django
from apps.music_app.models import Artist, Album, Song
from apps.user_app.models import User, Friend
from apps.playlist_app.models import Playlist, Addition, Listener

# a =  Artist.objects.filter().delete()
# for art in a:
#     art.name

# a =  Song.objects.all().delete()
# for art in a:
#     art.title

# users =  User.objects.get(id=3).delete()
# for user in users:
#     user.title

# playlist =  Playlist.objects.all().delete()
# for play in playlist:
#     play.title