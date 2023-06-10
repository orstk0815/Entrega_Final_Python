from django.urls import path
from tasks import views
from posts import views as posts_views


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("signin/", views.signin, name="signin"),
    path("posts/", posts_views.Posts, name="posts"),
    path("signin/posts/post", views.posts, name="signin_posts"),
]