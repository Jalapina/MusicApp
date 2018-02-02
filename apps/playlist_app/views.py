from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Playlist, Addition, Listener
# Create your views here.
def index(request):
    return render(request,'playlist_app/index.html')

def profile(request):
    return render(request,'user_app/profile.html')

def profile_edit(request):
    return render(request,'user_app/edit.html')

def playlist(request):
    if request.method=='POST':
        title=request.POST['playlist_name']
        playlist_description=request.POST['playlist_description']
        if len(title)>1:
            playlist=Playlist.objects.create(title=title, description=playlist_description)
            return redirect('main:playlist')
        else:
            messages.add_message(request,messages.ERROR, 'Title is too short')
            return redirect('main:playlist')
    context={
            'play': Playlist.objects.all()
    }

    return render(request, 'playlist_app/playlist.html', context)

def remove_playlist(request, playlist_id):
    Playlist.objects.get(id=playlist_id).delete()
    return redirect('main:playlist')


