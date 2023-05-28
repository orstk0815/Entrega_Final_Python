from django.shortcuts import render, redirect
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
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form":form}
    return render(request,"form_post.html",context )

def deletepost(request, pk):
    post = Posts.objects.get(id =pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    context = {"post":post}
    return render(request,"delete_posts.html", context)