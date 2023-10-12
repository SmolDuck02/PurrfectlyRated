from django.db import models

class ReviewPost(models.Model):
   post_picture = models.ImageField(upload_to='product_pictures/', blank=True, null=True)
   product_name = models.CharField(max_length=255)
   post_description = models.CharField(max_length=255)
   total_likes = models.IntegerField(null=True, blank=True)
   total_favorites = models.IntegerField(null=True, blank=True)

   def __str__(self):
    return self.product_name
