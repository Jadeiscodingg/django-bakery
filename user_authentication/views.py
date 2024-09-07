from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import MyUserCreationForm

# Create your views here.


def login_req(request):
    """
    This is the login section.
    Once user logs in it should authenticate the user.
    If the user is a verified registered user it should return to home page.
    If user is not registered an tries to log in it should give a error message.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            """
            If the user registers successfully the data should be saved.
            It should let the user login.
            Logged in, should return to the home page of the site.
            """
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


