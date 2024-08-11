from django.shortcuts import render, get_object_or_404
from .models import Product, Comment
from article.models import Category
from .forms import CommentForm
from home.models import BaseCategory
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Case, When, FloatField

def product(request):
    base_categories = BaseCategory.objects.all()
    if request.method == 'POST':
        search_query = request.POST['search_query']
        if len(search_query) >= 1:
            posts = Product.objects.filter(Q(title__icontains=search_query))
            context = {
                'posts' : posts,
                'query' : search_query,
                }
            return render(request, 'product.html', context)
    posts = Product.objects.all().annotate(stars=Avg(Case(When(comments__publish=True, then='comments__star'),output_field=FloatField())),)
    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'base_categories' : base_categories,
        'posts' : posts,
        'page_obj' : page_obj,
    }
    return render(request, "product.html", context)

def product_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    comments = post.comments.filter(publish=True)
    forms = Product.objects.all().annotate(stars=Avg(Case(When(comments__publish=True, then='comments__star'),output_field=FloatField())),)
    others = forms[:3]
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = post
            new_comment.save()
        else:
            print(comment_form.errors)
    context = {
        'post' : post,
        'comments' : comments,
        'others' : others,
    }
    return render(request, "product-detail.html", context)

def product_filter(request):
    categories = Category.objects.all()
    posts = Product.objects.all().annotate(stars=Avg(Case(When(comments__publish=True, then='comments__star'),output_field=FloatField())),)
    if request.method == 'POST':
        search_query = request.POST['search_query']
        if len(search_query) >= 1:
            posts = Product.objects.filter(Q(title__icontains=search_query))
            context = {
                'posts' : posts,
                'query' : search_query,
                'categories' : categories,
                }
            return render(request, 'product-filter.html', context)
    context = {
        'posts' : posts,
        'categories' : categories,
    }
    return render(request, "product-filter.html", context)