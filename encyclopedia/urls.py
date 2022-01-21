from re import search
from turtle import title
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.infopage, name="info"),
    path("search", views.search, name="searchpage"),
]
