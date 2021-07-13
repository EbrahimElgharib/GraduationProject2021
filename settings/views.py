from labs.models import Lab
from blog.models import Post
from django.shortcuts import render
from .models import Subscriber
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.http import JsonResponse
# Create your views here.


# def home(request):
#     places = Place.objects.all().annotate(property_count=Count('property_place'))
#     categorys = Category.objects.all()

#     # property list of every category
#     restaurant_list = Property.objects.filter(category__name='Restaurant')[:5]
#     hotels_list = Property.objects.filter(category__name='Hotels')[:4]
#     places_list = Property.objects.filter(category__name='Places')[:4]
#     recent_posts = Post.objects.all()[:4]

#     # count of propertys of every category
#     user_count = User.objects.all().count()
#     restaurant_count = Property.objects.filter(category__name='Restaurant').count()
#     hotels_count = Property.objects.filter(category__name='Hotels').count()
#     places_count = Property.objects.filter(category__name='Places').count()

#     context = {
#         'places':places,
#         'categorys':categorys,
#         'restaurant_list':restaurant_list,
#         'hotels_list':hotels_list,
#         'places_list':places_list,
#         'recent_posts':recent_posts,
#         'user_count':user_count,
#         'restaurant_count':restaurant_count,
#         'places_count':places_count,
#         'hotels_count':hotels_count,
#     }
#     return render(request, 'settings/home.html', context)

def home(request):
    context = {
        'recent_posts': Post.objects.all()[:3],
        'recent_labs': Lab.objects.all()[:3],
        'subscriber_form': SubscriberForm(),
    }
    return render(request, 'settings/home.html', context)


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
                        confirm your registration</a>.'.format(request.build_absolute_uri('/subscribe'),
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
    # else:
    #     print('no request yet')
    #     return {}

        
# confirm subscribers
def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'settings/home.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'settings/home.html', {'email': sub.email, 'action': 'denied'})

# delete subscribers
def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'settings/home.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'settings/home.html', {'email': sub.email, 'action': 'denied'})