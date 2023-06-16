from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("post/<str:id>", views.post, name="post"),
    path("form_post/", views.form, name="formPost"),
    path ("delete_post/<str:id>", views.deletepost, name="delete_post"),
    path('edit_view/<str:post_id>/', views.edit_post, name='edit_post'),
]