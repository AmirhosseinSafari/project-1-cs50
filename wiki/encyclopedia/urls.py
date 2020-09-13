from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entries_title>", views.entries, name="entries"),
    path("/search", views.entries_search, name="entries_search"),
    path("/new_page", views.create_new_page, name="new_page"),
    path("/new_page/saved_page", views.save_new_page, name="save_new_page")
]
