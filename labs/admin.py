from django.contrib import admin

# Register your models here.
from .models import Lab, Category
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description',)

admin.site.register(Lab, SomeModelAdmin)
admin.site.register(Category)