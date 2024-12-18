from django.shortcuts import render, get_object_or_404
from cart.models import Order
import requests
import json
from config.radman import DJANGO_ZARINPAL_MERCHANT_ID

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    
    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10
    
    zarinpal_request_url = 'https://payment.zarinpal.com/pg/v4/payment/request.json'
    
    request_header = {
        'accept' : 'application/json',
        'content-type' : 'application/json',
    }
    
    request_data = {
        'merchant_id' : DJANGO_ZARINPAL_MERCHANT_ID,
        'amount' : rial_total_price,
        'description' : f"#{order.id} : {order.user}",
        'callback_url' : 'https://aida-beauty7.ir',
    }
    
    response = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)