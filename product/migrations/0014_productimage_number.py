# Generated by Django 5.0.6 on 2024-08-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_productimage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='number',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6)], default=1, max_length=2, verbose_name='عدد عکس'),
            preserve_default=False,
        ),
    ]
