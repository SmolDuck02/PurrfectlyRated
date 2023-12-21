from django.contrib import admin
from .models import Users

# for display format  
class Admin(admin.ModelAdmin):
  list_display = ("category_name", "category_icon")
  

admin.site.register(Users)