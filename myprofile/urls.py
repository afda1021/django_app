#from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myprofile'

urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('', views.top, name='top'),
]