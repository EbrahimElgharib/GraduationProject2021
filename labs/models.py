from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
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

   # feature (slug) for url with title of post_detail
   slug = models.SlugField(null=True, blank=True)
   # for slug - save slug field = title of post
   def save(self, *args, **kwargs):
       if not self.slug:
          self.slug = slugify(self.title)
        # Call the real save() method
       super(Lab, self).save(*args, **kwargs)

   def __str__(self):
       return self.title

   def get_absolute_url(self):
       return reverse('labs:lab_detail',args=[str(self.slug)])



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
