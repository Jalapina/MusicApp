from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Artist,Album,Song,Fan

def index(request):#displays main music template and all music in the database
    if 'user_id' in request.session:
        context={
            'artists': Artist.objects.all()
        }
    return render(request,'music_app/index.html', context) 

def music(request):#Runs logic to add new Artist/album/year
    artist=request.POST['html_artist']
    album=request.POST['html_album']
    year=request.POST['album_year']
    auth =  True
    if len(artist)<1:
        auth = False
        messages.add_message(request,messages.ERROR,'Artist name is invalid')
    if len(album)<1:
        auth = False
        messages.add_message(request,messages.ERROR,'Album name is invalid')
    if len(year)<4 or len(year)>4:
        auth = False
        messages.add_message(request,messages.ERROR,'year is invalid')
    if auth == True:#adds everythng to the database
        try:
            artists=Artist.objects.create(name=artist)
            albums=Album.objects.create(title=album, year=year, artist_id=artists.id)
            context={
                'album_id':albums.id
            }
            url = reverse('music:song', kwargs=context)
            return redirect(url)
        except:
            messages.add_message(request,messages.ERROR,'Artist already exist')
            return redirect('music:home')     
    else:
        return redirect('music:home')

def adding_song(request, album_id):#Runs logic to add songs and renders templates
    if request.method=='POST':
        song = request.POST['html_song']
        genre = request.POST['html_genre']
        Song.objects.create(title=song, genre=genre, album_id=album_id)
        return redirect('music:song', album_id=album_id)

    context={
        'album': Album.objects.get(id=album_id),
        'songs': Song.objects.filter(album_id=album_id)
        }
    return render(request,'music_app/songs.html', context)
       
    



def add_artist(request, artist_id):#Runs login to add more albums to a specific Artist
    if request.method=='POST':
        album=request.POST['html_album']
        year=request.POST['html_year']
        
        if len(album)>1:
            Album.objects.create(title=album, year=year, artist_id=artist_id)
            return redirect('music:extra_add', artist_id=artist_id)
        else:
            messages.add_message(request,messages.ERROR,'Album name cannot be blank')
            return redirect('music:extra_add')
    context={
        'artist_id': Artist.objects.get(id=artist_id),
        'album_id': Album.objects.filter(artist_id=artist_id),
        'song_id': Song.objects.filter(album_id=artist_id)
        }
    return render(request,'music_app/artist.html', context)

def album(request, album_id):#Renders template to a specific album 
    if request.method=='POST':
        song =  request.POST['html_song']
        if len(song)>1:
            Song.objects.create(title=song, album_id=album_id)
            return redirect('music:albums', album_id=album_id)
        else:
            messages.add_message(request, messages.ERROR, 'Song name is too short')
            return redirect ('music:albums', album_id=album_id)
    context={
        'albums': Album.objects.get(id=album_id),
        'songs': Song.objects.filter(album_id=album_id)
    }
    return render(request, 'music_app/album.html', context)

def fans(request, artist_id):
    Fan.objects.create(artist_id=artist_id, user_id=request.session['user_id'])
    return redirect('music:extra_add', artist_id=artist_id )