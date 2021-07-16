from django import forms
from .models import Subscriber

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))