from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView
)
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class DetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'
