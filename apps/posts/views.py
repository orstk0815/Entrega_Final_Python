from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostForm

# Create your views here.

def home(request):
    post = Posts.objects.all()
    context = {"posts":post}
    return render(request, "posts/posts.html", context)

def post(request, id):
    post = Posts.objects.get(id=id)
    context = {"post":post}
    return render(request, "posts/article.html", context)

def form(request):
    form = PostForm()
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form":form}
    return render(request,"posts/form_post.html", context)

def edit_post(request, post_id):
    post = Posts.objects.filter(id=post_id).first()
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    context = {
        "form": form
    }
    return render(request, "posts/edit_post.html", context)

def deletepost(request, id):
    post = Posts.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    context = {"post":post}
    return render(request,"posts/delete_posts.html", context)