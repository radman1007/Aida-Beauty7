from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    text = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class BaseCategory(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    color = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name