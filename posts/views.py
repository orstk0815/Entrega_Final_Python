from django.shortcuts import render
from .models import Posts

# Create your views here.

def home(request):
    post = Posts.objects.all()
    context = {"posts":post}
    return render(request, "posts.html", context)

def article (request, pk):
    post = Posts.objects.get(id=pk)
    context = {"posts":post}
    return render(request, "article.html", context)
