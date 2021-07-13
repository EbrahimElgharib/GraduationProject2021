from settings.forms import SubscriberForm
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category, Lab
# Create your views here.

class LabList(ListView):
    model = Lab # model data
    paginate_by = 2 # pagination

    # return subscriber form in footer
    def get_context_data(self, **kwargs): # return another data
        context = super().get_context_data(**kwargs)
        context["subscriber_form"] = SubscriberForm()
        return context
        
class LabDetail(DetailView):
    model = Lab

    # return subscriber form in footer
    def get_context_data(self, **kwargs): # return another data
        context = super().get_context_data(**kwargs)
        context["subscriber_form"] = SubscriberForm()
        return context

def unity_lab(request):
    return render(request, 'labs/index.html',{})
