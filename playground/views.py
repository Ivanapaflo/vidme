from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def fetchVideo(request):
    first_video = Movie.objects.all().order_by('id').first()

    last_video = Movie.objects.all().order_by('id').last()

    show_next=False
    show_prev=False
    

    if last_video.id!=first_video.id:
        show_next=True

    return render(request, 'index.html', {'movie':first_video, 'nav':first_video.id, "show_prev":show_prev,"show_next": show_next})


@login_required(login_url='login')
def navigate(request, movie_id):
    movie=Movie.objects.get(id=movie_id)

    first_video = Movie.objects.all().order_by('id').first()

    last_video = Movie.objects.all().order_by('id').last()

    show_next=False
    show_prev=False
    
    if not first_video.id +1 > int(movie_id):
        show_prev=True

    if last_video.id!=movie.id:
        show_next=True

    return render(request, 'index.html', {'movie':movie, 'nav':movie_id, "show_prev":show_prev,"show_next": show_next})

def ulogin(request):
    if request.method=='POST':
       username= request.POST.get("username")
       password= request.POST.get("password")

       user= authenticate(request, username=username, password= password)

       if user is not None:
           login(request, user)
           return redirect('/')
    return render(request, 'login.html')

def register(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form': form}
    return render(request, 'register.html', context)


def ulogout(request):
        logout(request)
        return redirect("login")