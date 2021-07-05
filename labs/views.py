from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category, Lab
# Create your views here.

class LabList(ListView):
    model = Lab # model data
    paginate_by = 2 # pagination

class LabDetail(DetailView):
    model = Lab

def unity_lab(request):
    return render(request, 'labs/index.html',{})
