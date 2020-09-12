from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entries(request, entries_title):
    return render(request, "encyclopedia/entries.html", {
        "entry_content": util.get_entry(entries_title),
        "entries_title": entries_title
    })
