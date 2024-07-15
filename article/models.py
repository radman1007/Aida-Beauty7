from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title