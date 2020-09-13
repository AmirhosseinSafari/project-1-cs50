from django.shortcuts import render

from . import util


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
