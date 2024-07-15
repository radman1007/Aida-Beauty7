from django.shortcuts import render
from .models import Blog

def blog(request):
    forms = Blog.objects.all()
    context = {
        'forms' : forms,
    }
    return render(request, "blog.html", context)

def blog_filter(request):
    forms = Blog.objects.all()
    context = {
        'forms' : forms,
    }
    return render(request, "blog-filter.html", context)

def blog_detail(request, pk):
    
    return render(request, "blog-detail.html")