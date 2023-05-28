from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("post/<str:pk>", views.post, name="post"),
    path("form_post/", views.form, name="formPost"),
    path ("delete_post/<str:pk>", views.deletepost, name="delete_post"),
    
]