# from django.shortcuts import render
from settings.forms import SubscriberForm
from django.views.generic import ListView
from .models import About, Team, FAQ

# Create your views here.

class AboutList(ListView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        context["subscriber_form"] = SubscriberForm()
        return context

class FAQ(ListView):
    model = FAQ
