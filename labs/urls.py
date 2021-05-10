from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.LabList.as_view(), name='lab_list'),

]