from django.urls import path
from . import views

urlpatterns = [

     path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name="my-login"),
    path("userlogout", views.user_logout, name="logout"),
]