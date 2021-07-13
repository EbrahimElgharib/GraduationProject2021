from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Category, Lab
# Create your views here.

class LabList(ListView):# gets the ListView from django
    model = Lab # model data
    paginate_by = 2 # pagination

class LabDetail(DetailView):# gets the DetailView from django
    model = Lab

def unity_lab(request,lab_id):# renders the unity page
    return render(request, f'labs/index{lab_id}.html',{})#the link redirects depending on the desired lab
