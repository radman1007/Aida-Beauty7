from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product, name="product"),
    path('product-detail/<int:pk>', views.product_detail, name="product_detail"),
    path('product-filter/', views.product_filter, name="product_filter"),
]