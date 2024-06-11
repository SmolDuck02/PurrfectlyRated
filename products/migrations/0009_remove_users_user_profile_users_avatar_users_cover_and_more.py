# Generated by Django 4.2.5 on 2023-12-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_users_iscurrentuser_users_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='users',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='users',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]