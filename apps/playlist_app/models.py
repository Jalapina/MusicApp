from __future__ import unicode_literals
from ..music_app.models import Artist,Album,Song,Fan
from ..user_app.models import User, Friend
from django.db import models

class Playlist(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Addition(models.Model):
    song = models.ForeignKey(Song)
    playlist = models.ForeignKey(Playlist)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Listener(models.Model):
    user=models.ForeignKey(User, related_name='favorite_playlists')
    playlist=models.ForeignKey(Playlist, related_name='listeners')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

