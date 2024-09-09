from django.contrib import admin
from .models import Product, Comment, ProductImage
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali


class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['name', 'message', 'star', 'email', 'publish']
    extra = 1
    
    
class ProductImageInline(admin.StackedInline):
    model = ProductImage
    fields = ['image', 'number']
    extra = 1
    

@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'jcreated')
    ordering = ('-created',)
    inlines = [
        ProductImageInline,
        CommentsInline,
    ]
    @admin.display(description='زمان انتشار')
    def jcreated(self, obj):
        return datetime2jalali(obj.created).strftime('%d %b %Y')
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'star')
