from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.

# for contact-us page
def send_email(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # print('get request data is done')
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )
    # print('go return')
    return render(request, 'contact/contact.html', {})