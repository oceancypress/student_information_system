from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'professor'

urlpatterns = [
    path('', views.index, name='index'),
    path('sections', views.sections, name='sections'),
]
