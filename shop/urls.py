from django.urls import path,include
from django.contrib import admin
from . import views

"""
URL configuration for the application.

This module defines the URL patterns for the application and includes
routing to other URL configurations.

Imports:
-path: Django function for defining URL patterns.
-include: Django function for including other URL configurations.
-views: Module containing the view functions for the application.

URL patterns:
-'': Maps to the 'home' view.
-'auth/': Includes URL patterns from the 'user_authentication' app.
"""

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', include('user_authentication.urls')),
    path('admin/', admin.site.urls),   
]

