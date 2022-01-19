from re import search
from turtle import title
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.infopage, name="infopage"),
    path("search", views.searchpage, name="searchpage")
]
