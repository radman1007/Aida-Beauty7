from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="نام")
    last_name = models.CharField(max_length=250, verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="آدرس ایمیل")
    text = models.TextField(verbose_name="پیام")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'پیام کاربر'
        verbose_name_plural = 'پیام کاربر ها'
    
class BaseCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name="اسم")
    image = models.ImageField(verbose_name="عکس")
    color = models.CharField(max_length=20, null=True, blank=True, verbose_name="رنگ")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'دسته بندی پایه'
        verbose_name_plural = 'دسته بندی های پایه'
    
    
class News(models.Model):
    email = models.EmailField(verbose_name="آدرس ایمیل")
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'ایمیل خبرنامه'
        verbose_name_plural = 'ایمیل های خبرنامه'