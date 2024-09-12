from django.db import models

# Create your models here.

class Food(models.Model):
    """
    This is the model called Food which after should be registered in my admin.py.
    This holds the name, price,quanitity an the images of my products.

    Attributes:
        name (str): The name of the food product
        price(float): The price of the food product
        quantity(int): The quantity of the food product available
        image(str): A URL to an image of the food product
    """
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
