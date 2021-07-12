from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.

# choices of eductaion of users
EDUCATION = [
    ('ES', 'Elementary School'),
    ('MS', 'Middle School'),
    ('HS','High School'),
    ('U','University'),
    ('G','Graduate'),
]
class Profile(models.Model):
   # Relation One-to_One
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone_number = models.CharField(max_length=20, null=True, blank=True)
   image = models.ImageField(upload_to='users_image/', null=True, blank=True)
   address = models.CharField(max_length=50, null=True, blank=True)
   country = CountryField() 
   # city = models.CharField(max_length=50)
   # birth_date = models.DateField(max_length=10, null=True, blank=True) 
   education = models.CharField(max_length=2, choices=EDUCATION, null=True, blank=True)

   def __str__(self):
      return str(self.user)

### Signals
# create profile when Sign-Up
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



