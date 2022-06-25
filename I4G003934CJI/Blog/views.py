from django.shortcuts import render
from django.views.generic.edit import Create view
from . models import BlogApp
# Create your views here.


class PostListView(CreateView):
    model = Post


class PostCreateView(CreateView):
    model = Post

    fields = “__all__”

    success_url  = reverse_lazy(“blog:all”)


class PostDetailView(CreateView):
    model = Post
    

class PostUpdateView(CreateView):
    model = Post

    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”) 
    
    
class PostDeleteView(CreateView):
    models = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
    