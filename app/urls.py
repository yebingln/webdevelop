from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^logout/', views.logout),
    url(r'^login/', views.login),
    url(r'^index/', views.index),

]
