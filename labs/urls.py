from django.urls import path
from . import views

app_name = 'labs'

urlpatterns = [
    path('', views.LabList.as_view(), name='lab_list'),
    path('<slug:slug>',views.LabDetail.as_view(),name='lab_detail'),
]
