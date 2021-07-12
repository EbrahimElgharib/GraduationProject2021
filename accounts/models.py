# import all we need when creating models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

### Creating Our models here.

# choices of eductaion of users
EDUCATION = [
    # (stored value in DB, shown value in frontend),
    ('ES', 'Elementary School'), 
    ('MS', 'Middle School'),
    ('HS','High School'),
    ('U','University'),
    ('G','Graduate'),
]

# Model Class to Create a Prfile Table in DB
class Profile(models.Model):
   # Relation One-to_One with USER
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone_number = models.CharField(max_length=20, null=True, blank=True)
   image = models.ImageField(upload_to='users_image/', null=True, blank=True)
   address = models.CharField(max_length=50, null=True, blank=True)
   country = CountryField() # a package contains countries all over the world
   education = models.CharField(max_length=2, choices=EDUCATION, null=True, blank=True)

   # shown in admin panel
   def __str__(self):
      return str(self.user)

### Signals
# create a profile when Sign-Up a USER
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) # create a relation profile



