from django.db import models

class ProductCategory(models.Model):
  category_name = models.CharField(max_length=255)
  category_icon = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.category_name


class Product(models.Model):
   product_picture = models.ImageField(upload_to='product_pictures/', blank=True, null=True)
   product_name = models.CharField(max_length=255)
   product_description = models.CharField(max_length=255, null=True, blank=True)
   total_likes = models.IntegerField(null=True, blank=True)
   total_favorites = models.IntegerField(null=True, blank=True)
   total_reviews = models.IntegerField(null=True, blank=True)
   product_category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.DO_NOTHING)
   isDeleted = models.BooleanField(default=False)
   def __str__(self):
    return self.product_name

