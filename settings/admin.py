from django.contrib import admin
from .models import Subscriber, Newsletter, Website


# Register your models here.

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"

class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Website)
admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)