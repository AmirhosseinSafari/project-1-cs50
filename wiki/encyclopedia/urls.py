from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entries_title>", views.entries, name="entries"),
    path("search", views.entries_search, name="entries_search"),
    path("/new_page", views.create_new_page, name="new_page"),
    path("/new_page/saved_page", views.save_new_page, name="save_new_page"),
    path("<str:entries_title>/edit_page", views.edit_page, name="edit_page"),
    path("/random_page", views.random_page, name="random_page")
]

