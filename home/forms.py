from django import forms
from .models import Contact, News

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'