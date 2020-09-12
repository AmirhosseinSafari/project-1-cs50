from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entries(request, entries_title):

    print(str(util.get_entry(entries_title)))
    if(str(util.get_entry(entries_title)) != "None"):
        return render(request, "encyclopedia/entries.html", {
            "entry_content": util.get_entry(entries_title),
            "entries_title": entries_title
        })
    else:
        return render(request, "encyclopedia/pageNotFoundPage.html", {
            "entries_title": entries_title
        })
