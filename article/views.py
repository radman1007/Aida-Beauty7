from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, StaticBlog
from django.db.models import Q

def blog(request):
    statics = StaticBlog.objects.filter(accept=True)
    forms = Blog.objects.all().order_by('-created')
    top_two = forms[:2]
    others = forms[2:]
    context = {
        'statics' : statics,
        'top_two' : top_two,
        'others' : others,
    }
    return render(request, "blog.html", context)

def blog_filter(request):
    categories = Category.objects.all()
    forms = Blog.objects.all()
    if request.method == 'POST':
        search_query = request.POST['search_query']
        if len(search_query) >= 1:
            forms = Blog.objects.filter(Q(title__icontains=search_query))
            context = {
                'forms' : forms,
                'query' : search_query,
                'categories' : categories,
                }
            return render(request, 'blog-filter.html', context)
    if request.method == 'GET':
        search_category = request.GET.get('search_category')
        if search_category != None:
            forms = Blog.objects.filter(category__title__in=[search_category])
            context = {
                'forms' : forms,
                'categories' : categories,
                }
            return render(request, 'blog-filter.html', context)
    context = {
        'forms' : forms,
        'categories' : categories
    }
    return render(request, "blog-filter.html", context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    forms = Blog.objects.all()
    others = forms[:3]
    context = {
        'blog' : blog,
        'others' : others,
    }
    return render(request, "blog-detail.html", context)