from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import SignupForm
from .models import Profile

# Create your views here.

def signup(request):
       # check if form is submitted 
   if request.method == 'POST':
      # get request data
      form = SignupForm(request.POST)
      # check if form data is valid before save in DB
      if form.is_valid():
         form.save()
         # login after save
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         print('1')
         user = authenticate(username=username, password=password)
         print('2')
         login(request.user)
         print('3')
         return redirect('/accounts/profile')

      else:
         return render(request, 'registration/signup.html', {'form': form})
          
   else: # else return form as empty
      form = SignupForm()
      return render(request,'registration/signup.html',{'form':form})

# show profile data to user
def profile(request):
   profile = Profile.objects.get(user=request.user)
   context = {'profile':profile}
   return render(request, 'profile/profile.html',context)

# # show (Form) of all profile data to user
# def edit_profile(request):
#    # get profile data to show it in form
#    profile = Profile.objects.get(user=request.user)

#    if request.method == 'POST': # when click submit button
#       # get request data to check valid and save
#       profile_form = ProfileForm(request.POST, instance=profile)
#       user_form = UserForm(request.POST, instance=request.user)

#       # check valid --> save
#       if profile_form.is_valid() and user_form.is_valid():
#          user_form.save()
#          myprofile = profile_form.save(commit=False)
#          myprofile.user = request.user
#          myprofile.save()
      
#       # Go Back to profile.html
#       return redirect('/accounts/profile')

#    else: # when open page 
#       profile_form = ProfileForm(instance=profile)
#       user_form = UserForm(instance=request.user)
   
#    context = {
#       'profile_form':profile_form,
#       'user_form':user_form
#    }
#    return render(request, 'profile/profile_edit.html',context)
