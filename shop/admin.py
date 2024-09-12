from django.contrib import admin
from .models import Food
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Food model.

    This class customizes the admin interface for the Food model, allowing the name, price
    and qauntity fields to be displayed in the list view of the admin panel.
    """
    list_display = ('name', 'price', 'quantity')

# Register the Food model an its customized admin interface (FoodAdmin)
admin.site.register(Food, FoodAdmin)
