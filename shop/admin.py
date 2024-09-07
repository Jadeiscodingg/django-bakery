from django.contrib import admin
from .models import Food
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    """
    I added class FoodAdmin in the admin page so i could use list display.
    """
    list_display = ('name', 'price', 'quantity')



"""
registered my classes Food and FoodAdmin.
"""
admin.site.register(Food, FoodAdmin)
