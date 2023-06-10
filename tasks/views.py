from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.

def posts(request):
    return render(request, "posts.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
        "form": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("posts/post")
            except IntegrityError:
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "El usurio ya existe"
                    })
        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "El password no coincide"
            })


def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form" : AuthenticationForm
            })
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST.get("password", ""))
        if user is None:
            return render(request, "signin.html", {
                "form" : AuthenticationForm,   
                "error": "Su usuario o contraseña es incorrecto"
                })
        else:
            login(request, user)
            return redirect("posts/post")

