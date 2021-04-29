from django.db import models
from django.utils import timezone

# Create your models here.

### labs
class Lab(models.Model):
   title = models.CharField(max_length=50)
   description = models.TextField(max_length=20000)
   created_at = models.DateTimeField(default=timezone.now)
   image = models.ImageField(upload_to='images/')
   # doc_file = models.FileField(upload_to='doc_files/')

   # FK
   category = models.ForeignKey('Category', related_name='lab_category', on_delete=models.CASCADE)

   def __str__(self):
       return self.title
            

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name