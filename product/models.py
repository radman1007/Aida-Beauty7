from django.db import models
from django.urls import reverse
from accounts.models import User
from home.models import BaseCategory


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="اسم")
    image = models.ImageField(null=True,blank=True, verbose_name="عکس")
    price = models.PositiveIntegerField(default=0, verbose_name="قیمت")
    previous_price = models.PositiveIntegerField(verbose_name="قیمت قبلی", null=True, blank=True)
    body = models.TextField(verbose_name="توضیحات")
    category = models.ManyToManyField(BaseCategory, related_name='category', verbose_name="دسته بندی")
    available = models.BooleanField(default=True, verbose_name="موجود")
    weight = models.PositiveIntegerField(null=True, blank=True, verbose_name="وزن")
    mater = models.CharField(max_length=255, null=True, blank=True, verbose_name="مواد تشکیل دهنده")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
    

class Comment(models.Model):
    STAR_BOX = {
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
    }
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name="محصول")
    name = models.CharField(max_length=250, verbose_name="نام")
    message = models.TextField(verbose_name="پیام")
    email = models.EmailField(blank=True, null=True, verbose_name="آدرس ایمیل")
    star = models.CharField(max_length=2, choices=STAR_BOX, verbose_name="ستاره")
    publish = models.BooleanField(default=False, verbose_name="وضعیت انتشار")
    
    def __str__(self):
        return f"{self.name} : {self.message}"
    
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
