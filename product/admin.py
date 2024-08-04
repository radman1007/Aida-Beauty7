from django.contrib import admin
from .models import Product, Comment, Address

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created')
    ordering = ('-created',)
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'star')