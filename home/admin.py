from django.contrib import admin
from .models import Contact, BaseCategory, News, SliderImage


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    
    
admin.site.register(BaseCategory)
admin.site.register(News)


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')