# Generated by Django 4.2.5 on 2023-12-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
