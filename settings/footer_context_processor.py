from .models import Website, Subscriber
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.http import JsonResponse

# to return data to footer in base.html
# as it appear in all pages

def myfooter(request):
    myfooter = Website.objects.last()
    return {'myfooter':myfooter}


### Subscribers
# Generate tokens
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        ### check if email in database or not
        form = SubscriberForm(request.POST)
        print('SubscriberForm is get')
        if form.is_valid():
            print('form is valid')
            # check if email is unique or not
            new_email = form.cleaned_data['email']
            try:
                print("in try")
                email = Subscriber.objects.get(email=new_email)
                print("in try - before return")
                data = {'response_message': 'Email is subscribed already'}
                return JsonResponse(data)
                # return render(request, 'settings/subscribe.html', {'form': SubscriberForm()})
            except Subscriber.DoesNotExist:
                print("in except")
                sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
                sub.save()
                message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject='Newsletter Confirmation',
                    html_content='Thank you for signing up for my email newsletter! \
                        Please complete the process by \
                        <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                        confirm your registration</a>.'.format(request.build_absolute_uri('/subscriber/subscribe'),
                                                            sub.email,
                                                            sub.conf_num))
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                data = {'response_message': sub.email + 'is Successfully added - confirmation message is sent to email'}
                return JsonResponse(data)
                # return render(request, 'subscriber/subscribe.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    
        else:
            print('form is not valid')
            data = {'response_message': 'Email is Not Valid!'}
            return JsonResponse(data)
            # return render(request, 'subscriber/subscribe.html', {'message': 'Not Valid', 'form': SubscriberForm()})
    else:
        print('no request yet')
        return {'subscriber_form': SubscriberForm()}


# then go to setting.py ---> TEMPLATES --> options: --> 'settings.footer_context_processor.myfooter', # my footer