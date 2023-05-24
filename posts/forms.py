from django.forms import ModelForm
from django import forms
from .models import Posts

class PostForm (ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"
