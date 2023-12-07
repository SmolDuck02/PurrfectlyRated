# Generated by Django 4.2.5 on 2023-11-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_product_category_productcategory_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='isCurrentUser',
        ),
        migrations.AddField(
            model_name='users',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_profile',
            field=models.ImageField(blank=True, null=True, upload_to='user_profiles/'),
        ),
    ]