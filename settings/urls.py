from django.urls import path
from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/confirm/', views.confirm, name='confirm_subscribe'),
    path('subscribe/delete/', views.delete, name='delete_subscribe'),

]