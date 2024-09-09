from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Food
# Create your views here.

@login_required
def home(request):
    """
    Render the home page displaying all food objects.

    This view is decorated with 'login_required' to ensure that only authenticated
    users can access it. It retrieves all 'Food' objects from the database and passes 
    them to the 'home.html' template.

    Args:
        request (HttpRequest): The request object used to generate the reponse.

    Returns:
        HttpResponse: The rendered 'home.html' template with the food objects.
    """
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods})


