from django.shortcuts import render
from .models import About

# Create your views here.
def AboutView(request):
    return render(request, 'about.html', {})
