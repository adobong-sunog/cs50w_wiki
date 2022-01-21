from audioop import reverse
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def infopage(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/info.html", {
            "inform": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/noresult.html", {
            "invalid": title
        })

def search(request):
    search = request.GET.get("q")
    low = search.lower()
    entries = util.list_entries()
    lowercased = [i.lower() for i in entries]
    similar = []

    for i in entries:
        if low in i.lower():
            similar.append(i)

    for j in entries:
        if low in lowercased:
            return render(request, "encyclopedia/search.html", {
                "entry": util.get_entry(search)
            })
        elif similar != []:
            return render(request, "encyclopedia/similarity.html", {
                "searched": search,
                "close": similar
            })
        else:
            return render(request, "encyclopedia/noresult.html", {
            "invalid": search
        })
