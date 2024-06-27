from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('compare/', views.compare, name='compare'),
    path('faq/', views.faq, name='faq'),
]