from django.db import models
from django.utils import timezone


# Create your models here.
# About us
class About(models.Model):
   name = models.CharField(max_length=50)
   picture = models.ImageField(upload_to='pictures/')
   created_at = models.DateTimeField(default=timezone.now)
   description = models.TextField(max_length=500)
   job_type = models.CharField(max_length=100)
   birth_date = models.DateField()
   fb_link = models.URLField(max_length=200)
   wattsapp_link = models.URLField(max_length=200)
   linkedin_link = models.URLField(max_length=200)
