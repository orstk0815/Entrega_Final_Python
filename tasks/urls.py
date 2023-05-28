from django.urls import path
from tasks import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("signin/", views.signin, name="signin"),
]