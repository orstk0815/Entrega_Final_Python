from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def posts(request):
    return render(request, "posts.html")

