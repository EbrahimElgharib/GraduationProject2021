"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


settings


urlpatterns = [
    # accounts must be at first of all
    path('accounts/', include('django.contrib.auth.urls')), # User Auth
    path('accounts/', include('accounts.urls', namespace='accounts')), # Profile
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')), # summernote package for text editor in admin
    path('', include('settings.urls', namespace='home')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('labs/', include('labs.urls', namespace='labs')),
    path('about/',include('about.urls',namespace='about')),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
