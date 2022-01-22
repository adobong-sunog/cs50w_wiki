from re import search
from turtle import title
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.infopage, name="info"),
    path("search", views.search, name="searchpage"),
    path("new_entry", views.new, name="new"),
    path("save_entry", views.create, name="create"),
    path("edit_entry", views.edit, name="editpage"),
    path("save", views.save, name="saved"),
    path("random_entry", views.rand, name="random")
]
