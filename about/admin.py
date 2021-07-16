from django.contrib import admin

# Register your models here.
from .models import About, Team, FAQ

admin.site.register(About)
admin.site.register(Team)
admin.site.register(FAQ)
