from settings.forms import SubscriberForm
from django.shortcuts import render
from .models import Post, Category
from django.views.generic import DetailView, ListView

# Create your views here.
class PostList(ListView):
    model = Post
    paginate_by = 2

    # return subscriber form in footer
    def get_context_data(self, **kwargs): # return another data
        context = super().get_context_data(**kwargs)
        context["subscriber_form"] = SubscriberForm()
        return context



class PostDetail(DetailView):
    model = Post

    # return subscriber form in footer
    def get_context_data(self, **kwargs): # return another data
        context = super().get_context_data(**kwargs)
        context["subscriber_form"] = SubscriberForm()
        return context