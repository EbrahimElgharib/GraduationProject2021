from django.contrib import admin

# Register your models here.
from .models import About, Team

admin.site.register(About)
admin.site.register(Team)
