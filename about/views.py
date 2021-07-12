from django.views.generic import ListView
from .models import About, Team

class AboutList(ListView):
    model = Team # return team data
    # to return about site data 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        return context