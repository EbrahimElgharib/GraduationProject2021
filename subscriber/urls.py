from django.urls import path
from .views import subscribe, confirm, delete

app_name = 'subscriber'

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('subscribe/confirm/', confirm, name='confirm'),
    path('subscribe/delete/', delete, name='delete'),


]