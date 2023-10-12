from django.db import models
from products.models import Users

class Posts(models.Model):
   postUser = models.ForeignKey(Users, null=True, blank=True, on_delete=models.DO_NOTHING)
   

   #product_name = models.CharField(max_length=255)
   post_picture = models.ImageField(upload_to='product_pictures/', blank=True, null=True)
   post_description = models.CharField(max_length=255)
   total_likes = models.IntegerField(null=True, blank=True)
   total_favorites = models.IntegerField(null=True, blank=True)
   datetimePublished = models.DateTimeField(auto_now=True)
   is_shown = models.BooleanField(default=True)
   #no total_comments, will count and render it separately

   def __str__(self):
    return self.postUser.username 