from django.shortcuts import render, get_object_or_404
from .models import Product, Comment
from article.models import Category
from .forms import CommentForm

def product(request):
    posts = Product.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, "product.html", context)

def product_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    comments = post.comments.filter(publish=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = post
            new_comment.save()
    context = {
        'post' : post,
        'comments' : comments,
    }
    return render(request, "product-detail.html", context)

def product_filter(request):
    categories = Category.objects.all()
    posts = Product.objects.all()
    context = {
        'posts' : posts,
        'categories' : categories,
    }
    return render(request, "product-filter.html", context)