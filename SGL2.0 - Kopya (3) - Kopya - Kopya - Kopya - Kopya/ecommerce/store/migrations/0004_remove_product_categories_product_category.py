# Generated by Django 4.1.6 on 2023-09-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productcategory_alter_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Online Product', 'Online Product'), ('School Product', 'School Product')], max_length=100, null=True),
        ),
    ]
