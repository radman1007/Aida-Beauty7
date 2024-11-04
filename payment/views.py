from django.shortcuts import render, get_object_or_404
from cart.models import Order
import requests


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10
    
# https://payment.zarinpal.com/pg/v4/payment/request.json