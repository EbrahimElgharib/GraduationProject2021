from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category, Lab
from settings.forms import SubscriberForm
# Create your views here.

class LabList(ListView):# gets the ListView from django
    model = Lab # model data
    paginate_by = 3 # pagination

    # return subscriber form in footer
    def get_context_data(self, **kwargs): # return another data
        context = super().get_context_data(**kwargs)
        context["subscriber_form"] = SubscriberForm()
        return context

class LabDetail(DetailView):# gets the DetailView from django
    model = Lab

    # return subscriber form in footer
    def get_context_data(self, **kwargs): # return another data
        context = super().get_context_data(**kwargs)
        context["subscriber_form"] = SubscriberForm()
        return context

def unity_lab(request,lab_id):# renders the unity page
    return render(request, f'labs/index{lab_id}.html',{})#the link redirects depending on the desired lab
