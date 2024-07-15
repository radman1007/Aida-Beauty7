from django.shortcuts import render
from .models import Product
from article.models import Category

def product(request):
    posts = Product.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, "product.html", context)

def product_detail(request):
    return render(request, "product-detail.html")

def product_filter(request):
    categories = Category.objects.all()
    posts = Product.objects.all()
    context = {
        'posts' : posts,
        'categories' : categories,
    }
    return render(request, "product-filter.html", context)