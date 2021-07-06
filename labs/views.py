# from django.shortcuts import render
# from django.db.models.aggregates import Count
from django.shortcuts import render
from django.views.generic import DetailView, ListView
# from taggit.models import Tag
from .models import Category, Lab
# Create your views here.

class LabList(ListView):
    model = Lab # model data
    # paginate_by = 2 # pagination