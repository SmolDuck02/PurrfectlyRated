# Generated by Django 4.2.5 on 2023-12-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_users_user_profile_users_avatar_users_cover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='type',
            field=models.CharField(default='user', max_length=255),
        ),
    ]
