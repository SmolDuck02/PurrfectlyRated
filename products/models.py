from django.db import models

class ProductCategory(models.Model):
  category_name = models.CharField(max_length=255)
  category_icon = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.category_name

class Users(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  user_profile =  models.ImageField(upload_to='user_profiles/', blank=True, null=True)
  bio = models.CharField(max_length=255, null=True, blank=True)

  
  def __str__(self):
    return self.username + " " + self.password


class Product(models.Model):
   product_picture = models.ImageField(upload_to='product_pictures/', blank=True, null=True)
   product_name = models.CharField(max_length=255)
   product_description = models.CharField(max_length=255)
   total_likes = models.IntegerField(null=True, blank=True)
   total_favorites = models.IntegerField(null=True, blank=True)
   total_reviews = models.IntegerField(null=True, blank=True)
   product_category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.DO_NOTHING)
   
   def __str__(self):
    return self.product_name

