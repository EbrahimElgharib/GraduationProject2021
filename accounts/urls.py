from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns= [
   path('signup', views.signup, name='signup'),
   path('profile', views.profile, name='profile'),
   # path('profile/edit', views.edit_profile, name='edit_profile'),
]