from django.shortcuts import render
from .models import Subscriber

# Create your views here.

def home(request):
    return render(request, 'settings/home.html', {})



# confirm subscribers
def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'subscriber/subscribe.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'subscriber/subscribe.html', {'email': sub.email, 'action': 'denied'})

# delete subscribers
def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'subscriber/subscribe.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'subscriber/subscribe.html', {'email': sub.email, 'action': 'denied'})