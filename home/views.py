from django.shortcuts import render, redirect
from article.models import Blog
from .forms import ContactForm, NewsForm
from django.contrib.auth.decorators import login_required
from .models import BaseCategory

def index(request):
    forms = Blog.objects.all()
    base_categories = BaseCategory.objects.all()
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            news.save()
    context = {
        'forms' : forms,
        'base_categories' : base_categories,
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

@login_required()
def profile(request):
    return render(request, 'my-account.html')