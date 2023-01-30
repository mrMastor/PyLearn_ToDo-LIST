from django.shortcuts import render
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from mylist.models import ToList
from django.urls import reverse_lazy


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    count_item = ToList.objects.all().count()
    # Не выполненные задачи
    count_item_false = ToList.objects.filter(status=False).count()
    return render(
        request,
        "index.html",
        context={"count_item": count_item, "count_item_false": count_item_false},
    )


class ListListView(ListView):
    model = ToList
    fields = ["status", "name"]
    context_object_name = "full_lists"
    template_name = "todolist_full.html"


class ListViewFalse(ListView):
    model = ToList
    context_object_name = "list_false"
    queryset = ToList.objects.filter(status=False)
    template_name = "todolist.html"


class ItemCreateView(CreateView):
    model = ToList
    context_object_name = "add_item"
    fields = ["status", "name"]
    prepopulated_fields = {"slug": ["name"]}
    template_name = "item_create.html"


class ItemDetailView(DetailView):
    model = ToList
    context_object_name = "item_detail"
    template_name = "item_detail.html"


class ItemUpdateView(UpdateView):
    model = ToList
    fields = ["status", "name", "slug"]
    readonly_fields = (
        "date_create",
        "date_complite",
    )
    context_object_name = "item_update"
    template_name = "item_update.html"


class ItemDeleteView(DeleteView):
    model = ToList
    template_name = "item_delete.html"
    context_object_name = "item_delete"
    success_url = reverse_lazy("index")
