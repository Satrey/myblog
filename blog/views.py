from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Post

class BlogListView(ListView):

    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):

    model = Post
    template_name = 'detail.html'

class BlogCreateView(CreateView):

    model = Post
    template_name = 'create.html'
    fields = '__all__'