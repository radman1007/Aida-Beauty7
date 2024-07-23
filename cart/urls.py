from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
