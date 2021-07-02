from django.shortcuts import render
from .models import Post, Category
from django.views.generic import DetailView, ListView

# Create your views here.
class PostList(ListView):
    model = Post
    paginate_by = 3




class PostDetail(DetailView):
    model = Post
