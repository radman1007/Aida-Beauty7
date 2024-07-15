from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('blog-filter/', views.blog_filter, name="blog_filter"),
    path('blog-detail<', views.blog_detail, name="blog_detail"),
]