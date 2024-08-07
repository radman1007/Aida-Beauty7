from django.contrib import admin
from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'created')
    ordering = ('-created',)
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'star')
