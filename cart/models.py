from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
        
        
class Discount(models.Model):
    coupon_code = models.CharField(max_length=100, verbose_name="کد تخفیف")
    amount = models.PositiveIntegerField(default=0, verbose_name="مقدار تخفیف")
    limit = models.PositiveIntegerField(default=50, verbose_name="محدودیت تعداد")
    active = models.BooleanField(default=True, verbose_name="وضعیت")
    
    def __str__(self):
        return self.coupon_code
    
    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="orders", verbose_name="کاربر")
    first_name = models.CharField(max_length=100 ,verbose_name="نام")
    last_name = models.CharField(max_length=100 ,verbose_name="نام خانوادگی")
    city = models.CharField(max_length=100 ,verbose_name="شهر")
    address = models.CharField(max_length=700 ,verbose_name="آدرس")
    code = models.CharField(max_length=11, verbose_name="کد پستی")
    note = models.TextField(blank=True, null=True, verbose_name="متن خرید")
    paid = models.BooleanField(default=False ,verbose_name="وضعیت پرداخت")
    discount =  models.ForeignKey(Discount, on_delete=models.PROTECT, null=True, blank=True, related_name="orders", verbose_name="کد تخفیف")
    created = models.DateTimeField(auto_now_add=True ,verbose_name="زمان خرید")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان بروزرسانی")

    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name="محصول")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    price = models.PositiveIntegerField(default=0, verbose_name="قیمت")
    
    def __str__(self):
        return f"{self.product}"
    
    class Meta:
        verbose_name = 'موارد سفارش'
        verbose_name_plural = 'موارد سفارشات'