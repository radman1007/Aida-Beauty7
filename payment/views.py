from django.shortcuts import render, get_object_or_404
from cart.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)