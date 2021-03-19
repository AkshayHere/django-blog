from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about-us/', views.aboutUs, name='blog-about-us'),
]