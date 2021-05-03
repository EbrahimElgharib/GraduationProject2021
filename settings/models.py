from email.headerregistry import Address

from django.db import models

# Create your models here.

class Website(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(max_length=1000) 
   phone = models.CharField(max_length=20)
   Address = models.CharField(max_length=100)
   email = models.EmailField(max_length=254)
   logo = models.ImageField(upload_to='images/')
   fb_link = models.URLField(max_length=200)
   twitter_link = models.URLField(max_length=200)
   instagram_link = models.URLField(max_length=200)
