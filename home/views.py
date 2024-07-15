from django.shortcuts import render
from article.models import Blog

def index(request):
    forms = Blog.objects.all()
    context = {
        'forms' : forms
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def compare(request):
    return render(request, "compare.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    return render(request, "contact.html")