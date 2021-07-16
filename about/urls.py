from django.urls import path
from .views import AboutList, FAQ


app_name = 'about'

urlpatterns= [
   path('', AboutList.as_view(), name='about'),
   path('FAQ/', FAQ.as_view(), name='FAQ'),
]
