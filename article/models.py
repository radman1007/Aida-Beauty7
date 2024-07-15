from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True)
    author = models.CharField(max_length=250)
    body = models.TextField()
    category = models.ManyToManyField(Category, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", args={self.id})
    
    
class StaticBlog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True,blank=True)
    author = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    accept = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title