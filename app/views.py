from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView
)
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class DetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.author = User.objects.get(id=1)
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
