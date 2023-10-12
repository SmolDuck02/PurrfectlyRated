from django.contrib import admin
from .models import ProductCategory, Product, Users

# for display format  
class Admin(admin.ModelAdmin):
  list_display = ("category_name", "category_icon")
  

admin.site.register(ProductCategory, Admin)
admin.site.register(Product)
admin.site.register(Users)
