from django.shortcuts import render
from .models import Post, Category
from django.views.generic import DetailView, ListView

# Create your views here.
class PostList(ListView):
    model = Post






class PostDetail(DetailView):
    model = Post
