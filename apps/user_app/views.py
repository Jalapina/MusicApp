from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib import messages
import bcrypt
import re
from .models import User, Friend

REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request,'user_app/index.html')

def authentication(request):
    html_email=request.POST['html_email']
    server_password=request.POST['html_password']

    try:
        user = User.objects.get(email=html_email)
        if user.password == bcrypt.hashpw(server_password.encode('UTF-8'), user.password.encode('UTF-8')):
            request.session['user_id'] = user.id
            request.session['user_name'] = user.first_name
            return redirect('main:home')
        else:
            messages.add_message(request,messages.ERROR,'Invalid login')
            return redirect('user:home')
                      
    except:
        messages.add_message(request,messages.ERROR,'Email does not exist')
        return redirect('user:home')

    

def register(request):
    name=request.POST['html_name']
    last_name=request.POST['html_last_name']
    email=request.POST['html_email']
    password=request.POST['html_password']
    password_confirm=request.POST['html_confirm']
    auth = True

    if len(name)<1:
        auth=False
        messages.add_message(request,messages.ERROR,'Name is too short')
    if len(name)<1:
        auth=False
        messages.add_message(request,messages.ERROR,'Last name is too short')
    if not REGEX.match(email):
        auth=False
        messages.add_message(request,messages.ERROR,'Invalid Email')
    if len(password)<8:
        auth=False
        messages.add_message(request,messages.ERROR,'password must be at least 8 characters long')
    if password!=password_confirm:
        auth=False
        messages.add_message(request,messages.ERROR,'Password do not match')
    if auth == True:
        try:
            hashed_password=bcrypt.hashpw(password.encode('UTF-8'),bcrypt.gensalt())    
            user = User.objects.create(first_name=name,last_name=last_name , email=email,  password=hashed_password)
            request.session['user_id']=user.id
            request.session['user_name']=user.first_name
            return redirect('main:home')
        except:
             messages.add_message(request,messages.ERROR,'Email already exist!')
             return redirect('user:home')

    else:
        return redirect('user:home')



def edit(request):
    first_name=request.POST['html_name']
    last_name=request.POST['html_last_name']
    password=request.POST['html_password']
    password_confirm=request.POST['html_confirm']
    auth=True
    if len(first_name)<1:
        messages.add_message(request, messages.ERROR,'Name is too short')
        auth=False
    if len(last_name)<1:
        messages.add_message(request, messages.ERROR,'Last name is too short')
        auth=False
    if len(password)<8:
        messages.add_message(request, messages.ERROR,'password must be at least 8 charecters long')
        auth=False
    if password!=password_confirm:
        messages.add_message(request, messages.ERROR,'Passwords do not match')
        auth=False
    if auth==True:
        hashed_password=bcrypt.hashpw(password.encode('UTF-8'),bcrypt.gensalt()) 
        user = User.objects.get(id=request.session['user_id'])
        user.first_name=first_name
        user.last_name=last_name
        user.password=hashed_password
        user.save()
        request.session['user_id']=user.id
        request.session['user_name']=user.first_name

        return redirect('main:home')
    else:
        return redirect('main:profile')

    return redirect('main:home')

def logout(request):
    request.session.clear()
    return redirect('main:home')
    
def users(request):
    if 'user_id' in request.session:
        user = request.session['user_id']
        context={
            'profiles': User.objects.exclude(id=user).exclude(followers__follower_id=user),
            'follow': Friend.objects.filter(follower_id=user)
        }

    return render(request, 'user_app/users.html', context)

def following(request, followee_id):
    friends = Friend.objects.create(followee_id=followee_id, follower_id=request.session['user_id'])
    return redirect('user:users')

def unfollow(request,unfollow_id):
    Friend.objects.get( followee_id=unfollow_id ,follower_id=request.session['user_id']).delete()
    return redirect('user:users')
