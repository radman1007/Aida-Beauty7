from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from django.contrib import messages
from product.models import Product
from .forms import AddToCartProductForm, OrderForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Discount

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

@login_required()
def checkout(request):
    cart = Cart(request)
    order_form = OrderForm()
    context = {}
    if len(cart) == 0:
        messages.warning(request, 'سبد خرید شما خالی است.')
        return redirect('cart')
    if request.method == 'GET':
        coupon_code = request.GET.get('coupon_code')
        if coupon_code != None:
            discount = Discount.objects.filter(coupon_code=coupon_code).first()
            if discount == None:
                messages.warning(request, "این کد معتبر نیست.")
            else:
                if discount.active and discount.limit > 0:
                    discount_amount = discount.amount
                    discount.limit -= 1
                    discount.save()
                    context.update({
                        'discount_amount' : -discount_amount,
                    })
                    messages.success(request, "کد تخفیف اعمال شد.")
                else:
                    messages.warning(request, "این کد دیگر قابل استفاده نیست.")
    elif request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
                )
            cart.clear()
            messages.success(request, 'سفارش شما با موفقیت ثبت شد.')
            if len(request.user.fullname) == 0:
                request.user.fullname = f"{order_obj.first_name} {order_obj.last_name}"
                request.user.save()
            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')
    context.update({
        'cart' : cart,
        'form' : OrderForm(),
    })
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
        messages.warning(request, 'سبد خرید شما خالی است.')
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
    