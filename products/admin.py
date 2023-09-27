from django.contrib import admin
from .models import ProductCategory

class Admin(admin.ModelAdmin):
  list_display = ("product_category", )
admin.site.register(ProductCategory, Admin)
