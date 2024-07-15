from django.contrib import admin
from .models import Blog, Category

admin.site.register(Category)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')