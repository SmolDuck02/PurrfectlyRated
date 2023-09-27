from django.db import models

class ProductCategory(models.Model):
  product_category = models.CharField(max_length=255)


class Users(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  isCurrentUser = models.BooleanField(default=False)
