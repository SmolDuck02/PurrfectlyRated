# Generated by Django 4.2.5 on 2023-10-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_posts_is_shown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
