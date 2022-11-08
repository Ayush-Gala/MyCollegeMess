from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.login, name='login'),
    path("homepage", views.homepage, name='homepage'),
    path("signout", views.signout, name='signout'),
    path("feedback", views.feedback, name='feedback')
]
