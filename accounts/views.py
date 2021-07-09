from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, ProfileForm, UserForm
from .models import Profile

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import account_activation_token
from django.urls import reverse

# Create your views here.

def signup(request):
   # check if form is submitted 
   if request.method == 'POST':
      # get request data
      form = SignupForm(request.POST)
      # check if form data is valid before save in DB
      if form.is_valid():
         # form.save()
         # # login after save
         # username = form.cleaned_data['username']
         # password = form.cleaned_data['password1']
         print('1')
         # user = authenticate(username=username, password=password)
         # print('2')
         # login(request, user)
         # print('3')
         # return redirect('/accounts/profile')

         #test
         username = request.POST['username']
         email = request.POST['email']
         password = request.POST['password1']
         print('2')

         if not User.objects.filter(username=username).exists():
             print('3')
             if not User.objects.filter(email=email).exists():
                 print('4')
                 user = User.objects.create_user(username=username, email=email)
                 user.set_password(password)
                 user.is_active = False
                 user.save()
                 current_site = get_current_site(request)
                 print('5')
                 email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }

                 print('6') 
                 link = reverse('accounts:activate', kwargs={
                               'uidb64': email_body['uid'], 'token': email_body['token']})
                 print('7')
                 email_subject = 'Activate your account'

                 activate_url = 'http://'+current_site.domain+link

                 email = EmailMessage(
                    email_subject,
                    'Hi '+user.username + ', Please the link below to activate your account \n'+activate_url,
                    'ebrahimtest44@gmail.com',
                    [email],
                )
                 email.send(fail_silently=False)
                 messages.success(request, 'Account successfully created')
                 return render(request, 'registration/signup.html')

         return render(request, 'registration/signup.html')

          
   else: # else return form as empty
      form = SignupForm()
      
   return render(request,'registration/signup.html',{'form':form})



class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')

# # show profile data to user
# @login_required
# def profile(request):
#    profile = Profile.objects.get(user=request.user)
#    context = {'profile':profile}
#    return render(request, 'profile/profile.html',context)

# show (Form) of all profile data to user
@login_required
def profile(request):
   # get profile data to show it in form
   profile = Profile.objects.get(user=request.user)

   if request.method == 'POST': # when click submit button
      # get request data to check valid and save
      # request.FILES ---> to save uploaded files
      profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
      user_form = UserForm(request.POST, instance=request.user)
      print('post send')
      # check valid --> save
      if profile_form.is_valid() and user_form.is_valid():
         print('is valid')
         user_form.save()
         myprofile = profile_form.save(commit=False)
         myprofile.user = request.user
         myprofile.save()
      
         # # Go Back to profile.html
         # return redirect('/accounts/profile')

   else: # when open page 
      print('else not valid')
      profile_form = ProfileForm(instance=profile)
      user_form = UserForm(instance=request.user)
   
   context = {
      'profile_form':profile_form,
      'user_form':user_form
   }
   return render(request, 'profile/profile.html',context)









