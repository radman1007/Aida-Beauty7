from django.shortcuts import render, redirect
from article.models import Blog
from product.models import Product
from .forms import ContactForm, NewsForm
from .models import BaseCategory, SliderImage
from django.db.models import Avg, Case, When, FloatField
from django.contrib import messages

def index(request):
    sliders = SliderImage.objects.all()
    forms = Blog.objects.all()
    posts = Product.objects.all().annotate(stars=Avg(Case(When(comments__publish=True, then='comments__star'),output_field=FloatField())),)
    top_nine = posts[:9]
    after_nine = posts[9:12]
    base_categories = BaseCategory.objects.all()
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            news.save()
    context = {
        'sliders' : sliders,
        'forms' : forms,
        'base_categories' : base_categories,
        'top_nine' : top_nine,
        'after_nine' : after_nine,
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
            messages.success(request, 'پیام شما یا موفقیت ارسال شد.')
            return redirect('index')
    form = ContactForm()
    context = {
        'form' : form
    }
    return render(request, "contact.html", context)