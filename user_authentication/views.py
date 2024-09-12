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

    :param request: The HTTP request object
    :type request: HTTPRequest
    :returns: HTTP response to either the home page or login page with an error message
    :rtype: HttpResponse
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
    """
    Handle user registration and login.

    Processes the registration form, saves the new user if the form is valid, and 
    logs them in. If the form is invalid, displays an error messsage. After a succesful
    registration, the user is redirected to the home page.

    :param request: The HTTP request object
    :type request: HttpRequest
    :returns: HTTP reponse to either the home page or registration page with errors.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


