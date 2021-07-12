from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

### Lab Table
class Lab(models.Model):
   title = models.CharField(max_length=50)
   description = models.TextField(max_length=20000)
   created_at = models.DateTimeField(default=timezone.now)
   image = models.ImageField(upload_to='images/')
   youtube_url = models.URLField(max_length = 200,null=True)
   experiment_objective = models.TextField(max_length=1000,null=True)
   experiment_materials = models.TextField(max_length=1000,null=True)
   experiment_steps = models.TextField(max_length=1000,null=True)
   experiment_conclusion = models.TextField(max_length=1000,null=True)
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

   # to return id of every sepecific lab
   def get_absolute_url(self):
       return reverse('labs:lab_detail',args=[str(self.slug)])


# category of labs
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
