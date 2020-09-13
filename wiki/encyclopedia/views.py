from django.shortcuts import render

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
        
        file_name = entries_title + '.md'
        filepath = os.path.join('D:\edx\project1\wiki\entries', file_name)
        open(filepath, "a")

        return render(request , "encyclopedia/entries.html", {
            "entry_content": entries_content,
            "entries_title": entries_title
        })

    else:
        return render(request , "encyclopedia/messages.html", {
            "message_title": "Error:Page exist!",
            "message": "Page with \"" + entries_title + "\" exist!"
        })
