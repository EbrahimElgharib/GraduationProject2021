from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns= [
   path('signup/', views.signup, name='signup'),
   path('profile/', views.profile, name='profile'),

   path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name='activate'),
]