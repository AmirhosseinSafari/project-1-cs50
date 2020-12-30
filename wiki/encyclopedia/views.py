import random
from django.shortcuts import render, redirect

from . import util
import os


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entries(request, entries_title):

    if(str(util.get_entry(entries_title)) != "None"):
        return render(request, "encyclopedia/entries.html", {
            "entry_content": util.get_entry(entries_title),
            "entries_title": entries_title
        })
    else:
        return render(request, "encyclopedia/pageNotFoundPage.html", {
            "entries_title": entries_title
        })


def entries_search(request):

    entries_title = str(request.POST["entry"])

    if(str(util.get_entry(entries_title)) != "None"):
        return render(request, "encyclopedia/entries.html", {
            "entry_content": util.get_entry(entries_title),
            "entries_title": entries_title
        })
    else:
        entryies_list = []
        for entry in util.list_entries():
            if(entry.upper().find(entries_title.upper()) != -1):
                entryies_list.append(entry)
        return render(request, "encyclopedia/searchResults.html", {
            "entries": entryies_list,
            "entry_title": entries_title
        })


def create_new_page(request):
    return render(request, "encyclopedia/createNewPage.html")


def save_new_page(request):

    entries_title = str(request.POST["title_of_page"])
    entries_content = str(request.POST["content_of_page"])

    flag = False
    for entry in util.list_entries():
        if entry.upper() == entries_title.upper():
            flag = True

    if flag == False:

        util.save_entry(entries_title, entries_content)
        return render(request, "encyclopedia/entries.html", {
            "entries_title": entries_title,
            "entry_content": entries_content
        })

    else:
        return render(request, "encyclopedia/messages.html", {
            "message_title": "Error:Page exist!",
            "message": "Page with \"" + entries_title + "\" exist!"
        })


def edit_page(request, entries_title):

    if request.method == "POST":
        entries_content = str(request.POST["content_of_page"])
        util.save_entry(entries_title, entries_content)

        return render(request, "encyclopedia/entries.html", {
            "entry_content": util.get_entry(entries_title),
            "entries_title": entries_title
        })

    else:
        return render(request, "encyclopedia/editPage.html", {
            "previos_content": util.get_entry(entries_title),
            "title_entry": entries_title
        })


def random_page(request):
    list_entries = util.list_entries()
    rand_number = random.randint(0, len(list_entries)-1)
    entries_title = list_entries[rand_number]

    return redirect(entries, entries_title=entries_title)
    
