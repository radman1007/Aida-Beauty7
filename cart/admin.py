from django.contrib import admin
from .models import Order, OrderItem, Discount
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1
    

@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'city', 'created', 'paid')
    autocomplete_fields = ['user', 'discount']
    search_fields = ['user']
    inlines = [
        OrderItemInline,
    ]
    
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    autocomplete_fields = ['order', 'product']
    
    
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['coupon_code', 'amount', 'limit', 'active']
    search_fields = ['coupon_code']