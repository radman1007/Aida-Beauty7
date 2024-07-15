from django.shortcuts import render
from .models import Product

def product(request):
    posts = Product.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, "product.html", context)

def product_detail(request):
    return render(request, "product-detail.html")

def product_filter(request):
    return render(request, "product-filter.html")