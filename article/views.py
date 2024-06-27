from django.shortcuts import render

def blog(request):
    return render(request, "blog.html")

def blog_filter(request):
    return render(request, "blog-filter.html")
