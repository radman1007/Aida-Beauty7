from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True)
    price = models.PositiveIntegerField(default=0)
    body = models.TextField()
    weight = models.PositiveIntegerField()
    mater = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
