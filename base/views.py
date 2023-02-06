from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Band, Rhythm, Message, Music
from .forms import BandForm, MusicForm
# Create your views here.


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if not user:
            messages.error(request, 'User does not exist!')
            return render(request, 'base/login_register.html', {'page': page})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Password!')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, "An error occurred during registration")

    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    q = request.GET.get("q") if request.GET.get('q') != None else ""
    # i dont know why musics search is not working
    musics = Music.objects.filter(Q(name__icontains=q)) 
    bands = Band.objects.filter(Q(rhythm__name__icontains=q) | Q(name__icontains=q))
    rhythms = Rhythm.objects.all()
    band_count = bands.count()
    band_messages = Message.objects.filter(Q(band__rhythm__name__icontains=q))

    context = { 'musics': musics, 'bands': bands, 'rhythms': rhythms,
     'band_count' : band_count, 'band_messages':band_messages}
    return render(request, 'base/home.html', context)

def band(request, pk):
    band = Band.objects.get(id=pk)
    musics = Music.objects.filter(band__id=pk)
    band_messages = band.message_set.all()
    participants = band.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            band = band,
            body=request.POST.get('body')
        )
        band.participants.add(request.user)
        return redirect('band', pk=band.id)

    context = {'band' : band, 'band_messages': band_messages, 'participants':participants, "musics": musics}
    return render(request, "base/band.html", context)

@login_required(login_url='login')
def music(request, pk):
    music = Music.objects.get(id=pk)

    context = {'music' : music}
    return render(request, "base/music.html", context)


@login_required(login_url='login')
def createBand(request):
    form = BandForm()
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save(commit=False)
            band.host = request.user
            band.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/band_form.html', context)

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    bands = user.band_set.all()
    band_messages = user.message_set.all()
    rhythm = Rhythm.objects.all()
    context = {'user': user, 'bands': bands, 'band_messages': band_messages,
     'rhythm': rhythm}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def updateBand(request,pk):
    band = Band.objects.get(id=pk)
    form = BandForm(instance=band)

    if request.user != band.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/band_form.html', context)

@login_required(login_url='login')
def deleteBand(request, pk):
    band = Band.objects.get(id=pk)

    if request.method == 'POST':
        band.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':band} )

@login_required(login_url='login')
def createMusic(request):
    form = MusicForm()
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/music_form.html', context)

@login_required(login_url='login')
def updateMusic(request,pk):
    music = Music.name.get(id=pk)
    form = MusicForm(instance=music)

    if request.method == 'POST':
        form = MusicForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/music_form.html', context)

@login_required(login_url='login')
def deleteMusic(request, pk):
    music = Music.name.get(id=pk)

    if request.method == 'POST':
        music.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':music} )

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':message} )

