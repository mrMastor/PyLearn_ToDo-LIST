from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("full-list/", views.ListListView.as_view(), name="full_list"),
    re_path(r"^list/$", views.ListViewFalse.as_view(), name="list_false"),
    re_path(r"^add/$", views.ItemCreateView.as_view(), name="add_item"),
    path("<str:slug>/edit/", views.ItemUpdateView.as_view(), name="item_update"),
    path("<str:slug>/", views.ItemDetailView.as_view(), name="item_detail"),
    path("<str:slug>/delete/", views.ItemDeleteView.as_view(), name="item_delete"),
]
