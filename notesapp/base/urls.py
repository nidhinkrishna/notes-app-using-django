from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Homepage,name='home'),
    path('signup/',views.signup,name='signup'),
    
]
