from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entries_title>", views.entries, name="entries")
]
