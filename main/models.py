


from django.db import models
from authentication.models import Users
# from products.models import Users

class Posts(models.Model):
    post_user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    post_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    post_description = models.CharField(max_length=255)
    total_likes = models.IntegerField(null=True, blank=True, default=0)
    total_dislikes = models.IntegerField(null=True, blank=True, default=0)
    total_favorites = models.IntegerField(null=True, blank=True)
    datetime_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        post_desc_preview = self.post_description if len(self.post_description) < 70 else self.post_description[:70]
        return self.post_user.username + ": " + post_desc_preview
    
class Interaction(models.Model):
    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, null=True, blank=True, on_delete=models.CASCADE)

    is_post_shown = models.BooleanField(default=False)
    is_post_liked = models.BooleanField(default=False)
    is_post_disliked = models.BooleanField(default=False)
    is_post_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} -> {self.post.__str__()}"
    

class Comments(models.Model):
    comment_user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    comment_description = models.CharField(max_length=255)
    datetime_published = models.DateTimeField(auto_now_add=True)
    comment_replies = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        comment_desc_preview = self.comment_description if len(self.comment_description) < 70 else self.comment_description[:70]
        return self.comment_user.username + ": " + comment_desc_preview 