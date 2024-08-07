from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="اسم")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="اسم")
    image = models.ImageField(null=True,blank=True, verbose_name="عکس")
    author = models.CharField(max_length=250, verbose_name="نویسنده")
    body = RichTextField(verbose_name="توضیحات")
    category = models.ManyToManyField(Category, related_name='category', verbose_name="دسته بندی ها")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان بروزرسانی")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", args={self.id})
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
    
    
class StaticBlog(models.Model):
    title = models.CharField(max_length=250, verbose_name="اسم")
    image = models.ImageField(null=True,blank=True, verbose_name="عکس")
    author = models.CharField(max_length=250, verbose_name="نویسنده")
    body = RichTextField(verbose_name="توضیحات")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان انتشار")
    accept = models.BooleanField(default=False, verbose_name="تایید شده")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مقاله پایه'
        verbose_name_plural = 'مقاله های پایه'