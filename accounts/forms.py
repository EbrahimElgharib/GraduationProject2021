from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.widgets import CountrySelectWidget

# signup
class SignupForm(UserCreationForm):
   # to remove help_text of password
   password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
   password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)

   # form
   class Meta:
      model = User
      fields = ['username', 'email','password1']
      # fields = ['first_name','last_name','username', 'email','password1']

              

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      # fields = ['username','email','first_name','last_name'] 
      fields = ['email','first_name','last_name'] 

class ProfileForm(forms.ModelForm):
   image = forms.ImageField(error_messages={'invalid':("Image Files Only!")}, widget=forms.FileInput)
   class Meta:
      model = Profile
      # fields = ['image', 'phone_number','country', 'address','education']
      fields = ['image','phone_number','country']
      # fields = ['user','phone_number','address','image']
      widgets = {'country': CountrySelectWidget()} # for country pkg