from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .form import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def land(request):
    return render(request, 'land.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfull')
            return redirect('/front')
        else:
            messages.info(request, 'somthing went wrong try again')
            error_message = form.errors.as_text()
            return render(request, 'land.html', {'error': error_message})

    return render(request, 'land.html')

def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/front")
        else:
            messages.info(request, 'RECORD NOT FOUND')
            return redirect('/')

    return render(request, 'land.html')
@login_required
def front(request):
    return render(request, 'front.html')

@login_required
def index(request):
    return render(request, 'index.html', {'displayName': request.user.first_name + " " + request.user.last_name})

@login_required
def room(request):
    return render(request, 'room.html')
