# Generated by Django 4.2.5 on 2023-12-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_isdeleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
