from django.db import models

class Users(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  avatar =  models.ImageField(upload_to='avatars/', blank=True, null=True)
  cover = models.ImageField(upload_to='covers/', blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  bio = models.CharField(max_length=255, null=True, blank=True)
  type = models.CharField(max_length=255, default='user')
  
  
  def __str__(self):
    return self.username + " " + self.password