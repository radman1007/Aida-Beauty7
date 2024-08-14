from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.contrib import messages
from product.models import Product
from .forms import AddToCartProductForm
from django.views.decorators.http import require_POST

def cart(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(
            initial={
                'quantity' : item['quantity'],
                'inplace' : True,
            }
        )
    context = {
        'cart' : cart,
    }
    return render(request, "cart.html", context)

def checkout(request):
    cart = Cart(request)
    context = {
        'cart' : cart,
    }
    return render(request, "checkout.html", context)

@require_POST
def cart_add(request, product_id):
    next_page = request.POST.get('next_page')
    print(request.POST.get('quantity'))
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, cleaned_data['inplace'])
    if next_page != None:
        return redirect(next_page)
    return redirect('cart')

def cart_clear(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty')
        return redirect('index')
    cart.clear()
    messages.success(request, '')
    return redirect('index')

@require_POST
def cart_remove(request, product_id):
    next_page = request.POST.get('cart_base')
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    if next_page != None:
        return redirect(next_page)
    return redirect('cart')
    