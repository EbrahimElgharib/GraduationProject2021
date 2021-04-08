from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'AboutUs.html')

def signup_view(request):
    return render(request,'SignUp.html')

def blog_view(request):
    return render(request,'Blogs.html')

def labs_view(request):
    return render(request,'Virtual_Laps.html')
