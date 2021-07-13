# from django.shortcuts import render
from django.views.generic import ListView
from .models import About, Team, FAQ

# Create your views here.

class AboutList(ListView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        return context

class FAQ(ListView):
    model = FAQ
