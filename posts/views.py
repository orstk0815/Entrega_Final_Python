from django.shortcuts import render
from .models import Posts
from .forms import PostForm

# Create your views here.

def home(request):
    post = Posts.objects.all()
    context = {"posts":post}
    return render(request, "posts.html", context)

def post (request, pk):
    post = Posts.objects.get(id=pk)
    context = {"post":post}
    return render(request, "article.html", context)

def form(request):
    form = PostForm()
    context = {"form":form}
    return render(request,"form_post.html",context )