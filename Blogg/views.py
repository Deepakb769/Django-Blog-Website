from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render (request, "Blogg/entry.html",)

def about(request):
    return render (request, 'Blogg/about.html' , {'title' : 'About'})

class PostListView(ListView):  # A list view
    model = Post
    template_name = 'Blogg/entry.html'
    context_object_name = 'posts'
    order = ['-date_posted'] # This will provide updated at the top everytime when a post is made

class PostDetailView(DetailView):  # A list view
    model = Post

class PostCreateView(CreateView):  
    model = Post
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
