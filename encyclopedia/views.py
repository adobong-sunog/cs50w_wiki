from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def infopage(request, title):
    return render(request, "encyclopedia/info.html", {
        "inform": util.get_entry(title)
    })