from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [

    path('login/',login_view, name="login"),
    path('logout/',logout_view,name="logout"),
    path('register/',register_view,name="signup"),
]
