from .models import Website

# to return data to footer in base.html
# as it appear in all pages

def myfooter(request):
    myfooter = Website.objects.last()
    return {'myfooter':myfooter}

# then go to setting.py ---> TEMPLATES --> options: --> 'settings.footer_context_processor.myfooter', # my footer