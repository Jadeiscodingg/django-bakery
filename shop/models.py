from django.db import models

# Create your models here.

class Food(models.Model):
    """
    This is the model called Food which after should be registered in my admin.py.
    This holds the name, price,quanitity an the images of my products.

    Attributes:
    :param name: The name of the food product
    :type name: str
    :param price: The price of the food product
    :type price: float
    :param quantity: The qauntity of the food product
    :type qauntity: int
    :param image: A URL to an image of the food product
    :type image: str
    """
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
