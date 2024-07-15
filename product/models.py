from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True)
    price = models.PositiveIntegerField(default=0)
    body = models.TextField()
    weight = models.PositiveIntegerField()
    mater = models.CharField(max_length=255)