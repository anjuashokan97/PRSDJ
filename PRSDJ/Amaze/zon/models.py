from django.db import models


# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class Card(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=3000)
