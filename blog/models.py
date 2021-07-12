from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from taggit.managers import TaggableManager

#### Post Table
class Post(models.Model):
    # FK
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    # FK
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    # rows
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=20000)
    tags = TaggableManager() # tags from external package

    # feature (slug) for url with title of post_detail
    slug = models.SlugField(null=True, blank=True)

    # for slug - save slug field = title of post
    def save(self, *args, **kwargs):
        if not self.slug:
               self.slug = slugify(self.title)
        # Call the real save() method
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[str(self.slug)])

# Category of Posts
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
