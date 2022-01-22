from audioop import reverse
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util
import encyclopedia

import random
import markdown
from markdown2 import Markdown
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def infopage(request, title):
    find = util.get_entry(title)
    if find != None:
        converted = markdown.markdown(find)
        return render(request, "encyclopedia/info.html", {
            "inform": converted,
            "named": title
        })
    else:
        return render(request, "encyclopedia/noresult.html", {
            "invalid": title
        })

def search(request):
    search = request.GET["q"]
    low = search.lower()
    entries = util.list_entries()
    lowercased = [i.lower() for i in entries]
    similar = []
    raw = util.get_entry(search)

    for i in entries:
        if low in i.lower():
            similar.append(i)

    for j in entries:
        if low in lowercased:
            convert = markdown.markdown(raw)
            return render(request, "encyclopedia/search.html", {
                "entry": convert,
                "named": search
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

def new(request):
    return render(request, "encyclopedia/newentry.html")

def create(request):
    if request.method == "POST":
        name = request.POST["entrytitle"]
        desc = request.POST["entrydesc"]
        entries = util.list_entries()
        same = "none"

        for i in entries:
            if name.lower() == i.lower():
                same = "have"
        
        if same == "have":
            return render(request, "encyclopedia/exists.html", {
                "name": name
            })
        else:
            util.save_entry(name, desc)
            raw = util.get_entry(name)
            return render(request, "encyclopedia/info.html", {
                "inform": markdowner.convert(raw)
            })

def edit(request):
    if request.method == "POST":
        name = request.POST["etitle"]
        return render(request, "encyclopedia/edit.html", {
            "page": util.get_entry(name),
            "titlename": name
        })

def save(request):
    if request.method == "POST":
        new = request.POST["edited"]
        newtitle = request.POST["nametitle"]
        util.save_entry(newtitle, new)
        raw = util.get_entry(newtitle)
        return render(request, "encyclopedia/info.html", {
            "inform": markdowner.convert(raw),
            "named": newtitle
        })

def rand(request):
    choice = util.list_entries()
    randchoice = random.choice(choice)
    raw = util.get_entry(randchoice)
    return render(request, "encyclopedia/info.html", {
        "inform": markdowner.convert(raw),
        "named": randchoice
    })