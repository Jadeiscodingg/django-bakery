from django.db import models

# Create your models here.

class Food(models.Model):
    """
    This is the model called Food which after should be registered in my admin.py.
    This holds the name, price,quanitity an the images of my products.
    """
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
