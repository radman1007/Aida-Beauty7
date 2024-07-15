from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, StaticBlog

def blog(request):
    statics = StaticBlog.objects.filter(accept=True)
    forms = Blog.objects.all()
    context = {
        'statics' : statics,
        'forms' : forms,
    }
    return render(request, "blog.html", context)

def blog_filter(request):
    categories = Category.objects.all()
    forms = Blog.objects.all()
    context = {
        'forms' : forms,
        'categories' : categories
    }
    return render(request, "blog-filter.html", context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog' : blog
    }
    return render(request, "blog-detail.html", context)