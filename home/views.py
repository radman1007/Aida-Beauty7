from django.shortcuts import render
from article.models import Blog
from product.models import Product

def index(request):
    posts = Product.objects.all()
    forms = Blog.objects.all()
    context = {
        'posts' : posts,
        'forms' : forms,
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