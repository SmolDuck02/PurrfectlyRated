# Generated by Django 4.2.5 on 2023-12-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(default='user', max_length=255)),
            ],
        ),
    ]