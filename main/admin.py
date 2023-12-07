from django.contrib import admin
from .models import Comments, Interaction, Posts
# Register your models here.

admin.site.register(Posts)
admin.site.register(Interaction)
admin.site.register(Comments)