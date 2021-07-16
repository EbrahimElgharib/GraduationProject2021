from django.db import models
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from django.conf import settings

# Create your models here.


class Website(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(max_length=1000) 
   phone = models.CharField(max_length=20)
   Address = models.CharField(max_length=100)
   email = models.EmailField(max_length=254)
   logo = models.ImageField(upload_to='images/')
   fb_link = models.URLField(max_length=200)
   twitter_link = models.URLField(max_length=200)
   instagram_link = models.URLField(max_length=200)

   def __str__(self):
      return str(self.id)


# Subscribe with Emails
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


# Newsletter file send to all subscribers
class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='uploaded_newsletters/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    # send func to send messages to subscribers
    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        # send message to all subscribers
        for sub in subscribers:
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/subscribe'),
                            sub.email,
                            sub.conf_num))
            sg.send(message) # send it now