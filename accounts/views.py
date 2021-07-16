from settings.forms import SubscriberForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ProfileForm, UserForm
from .models import Profile
from django.conf import settings
from .decorators import check_recaptcha

from verify_email.email_handler import send_verification_email

# signup view 
@check_recaptcha # recaptcha api for security and stability
def signup(request):
   # check if form is submitted 
   if request.method == 'POST':
      # get request data
      form = SignupForm(request.POST)
      # check if form data is valid before save in DB
      # and check if recaptcha is success or not for secure
      if form.is_valid() and request.recaptcha_is_valid:
         # login after save data of user
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         email = form.cleaned_data.get('email')
         try:
            test = User.objects.get(email=email)
            messages.error(request, 'This email is signned up already')
         except:
            # form.save() # save a form
            ### login in now
            # user = authenticate(username=username, password=password)
            # login(request, user)

            inactive_user = send_verification_email(request, form) # verify pkg
            # inactive_user.cleaned_data['email']

            return redirect('/accounts/profile')  
   else: # else return form as empty
      form = SignupForm()
   return render(request,'registration/signup.html',{'form':form})


# show (Form) of all profile data to user
# can edit data and submit it or reset it 
@login_required
def profile(request):
   # get profile data to show it in form
   profile = Profile.objects.get(user=request.user)

   if request.method == 'POST': # when click submit button
      # get request data to check valid and save
      # request.FILES ---> to save uploaded files/pictures
      profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
      user_form = UserForm(request.POST, instance=request.user)
      print('post send')
      # check valid --> save
      if profile_form.is_valid() and user_form.is_valid():
         # save/update forms/data of user
         user_form.save()
         myprofile = profile_form.save(commit=False)
         myprofile.user = request.user
         myprofile.save()

   else: # when open page without any submitted button
      print('else not valid')
      profile_form = ProfileForm(instance=profile)
      user_form = UserForm(instance=request.user)
   
   context = {
      'profile_form':profile_form,
      'user_form':user_form,
      'subscriber_form': SubscriberForm()
   }
   return render(request, 'profile/profile.html',context)









