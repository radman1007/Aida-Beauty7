from django.shortcuts import render

def product(request):
    return render(request, "product.html")

def product_detail(request):
    return render(request, "product-detail.html")