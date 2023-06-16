from django.urls import path
from .views import *
from apps.posts import views as posts_views


urlpatterns = [
    path("posts/", posts_views.Posts, name="posts"),
    path("signin/posts/post", posts, name="signin_posts"),
]