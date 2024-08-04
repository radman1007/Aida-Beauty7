from django.contrib import admin
from .models import Contact, BaseCategory

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    
    
admin.site.register(BaseCategory)