from django.shortcuts import render, redirect
from article.models import Blog
from product.models import Product
from .forms import ContactForm

def index(request):
    forms = Blog.objects.all()
    context = {
        'forms' : forms,
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {
        'form' : form
    }
    return render(request, "contact.html", context)