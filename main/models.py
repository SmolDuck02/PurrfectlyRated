


from django.db import models
from products.models import Users

class Posts(models.Model):
    postUser = models.ForeignKey(Users, null=True, blank=True, on_delete=models.DO_NOTHING)
    post_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    post_description = models.CharField(max_length=255)
    total_likes = models.IntegerField(null=True, blank=True, default=0)
    total_dislikes = models.IntegerField(null=True, blank=True, default=0)
    total_favorites = models.IntegerField(null=True, blank=True)
    datetimePublished = models.DateTimeField(auto_now=True)
    is_shown = models.BooleanField(default=True)

    def __str__(self):
        return self.postUser.username