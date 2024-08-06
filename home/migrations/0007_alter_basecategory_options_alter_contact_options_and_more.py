# Generated by Django 5.0.6 on 2024-08-06 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_news_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basecategory',
            options={'verbose_name': 'دسته بندی پایه', 'verbose_name_plural': 'دسته بندی های پایه'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'پیام کاربر', 'verbose_name_plural': 'پیام کاربر ها'},
        ),
        migrations.AlterField(
            model_name='basecategory',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='basecategory',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='basecategory',
            name='name',
            field=models.CharField(max_length=250, verbose_name='اسم'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='آدرس ایمیل'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=250, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.TextField(verbose_name='پیام'),
        ),
    ]