from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Food
# Create your views here.

@login_required
def home(request):
    """
    This is the home page which contains all my objects.
    In my home html page would contain the images ect.
    food is the variable that holds all the objects set from my model Food.
    """
    food = Food.objects.all()
    return render(request, 'home.html', {'food': food})


