# Generated by Django 4.2.5 on 2023-11-06 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_users_iscurrentuser_users_bio_and_more'),
        ('main', '0007_posts_is_disliked_posts_is_favorite_posts_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='is_disliked',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='is_favorite',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='is_liked',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='is_shown',
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_post_shown', models.BooleanField(default=False)),
                ('is_post_liked', models.BooleanField(default=False)),
                ('is_post_disliked', models.BooleanField(default=False)),
                ('is_post_favorite', models.BooleanField(default=False)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.posts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.users')),
            ],
        ),
    ]