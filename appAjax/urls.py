from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^ajax/', views.ajax),
    url(r'^rout/', views.rout),


]
