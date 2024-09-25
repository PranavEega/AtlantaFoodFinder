from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('finder/dashboard/', views.dashboard, name='dashboard'),

    path('add-favorite/', views.add_favorite, name='add_favorite'),
]