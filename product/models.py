from django.db import models
from django.urls import reverse
from accounts.models import User
from home.models import BaseCategory


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True)
    price = models.PositiveIntegerField(default=0)
    body = models.TextField()
    category = models.ManyToManyField(BaseCategory, related_name='category')
    weight = models.PositiveIntegerField()
    mater = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    STAR_BOX = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
    }
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=250)
    message = models.TextField()
    email = models.EmailField(blank=True, null=True)
    star = models.CharField(max_length=2, choices=STAR_BOX)
    publish = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} : {self.message}"
    
    
# class Order(models.Model):
#     ORDER_STATUS_PAID = 'p'
#     ORDER_STATUS_UNPAID = 'u'
#     ORDER_STATUS_CANCELED = 'c'
#     ORDER_STATUS = [
#         (ORDER_STATUS_PAID,'Paid'),
#         (ORDER_STATUS_UNPAID,'Unpaid'),
#         (ORDER_STATUS_CANCELED,'Canceled'),
#     ]
    
#     user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
#     datetime_created = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=1, choices=ORDER_STATUS, default=ORDER_STATUS_UNPAID)
    
    
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
#     quantity = models.PositiveSmallIntegerField()

#     class Meta:
#         unique_together = [['order', 'product']]


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    city = models.CharField(max_length=250)
    text = models.TextField()
    house_number = models.CharField(max_length=11)
    
    def __str__(self):
        return f"{self.user.fullname} : {self.city}"