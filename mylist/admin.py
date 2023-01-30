from mylist.models import ToList
from django.contrib import admin
from django.utils import timezone


@admin.action(description="Выполнено")
def deactivate(modeladmin, request, queryset):
    """Кастомное действие в админке - деактивация выбранных задач."""
    count = queryset.update(status=True, date_complite=timezone.now())
    modeladmin.message_user(request, f"Было обновлено {count} записей")


@admin.action(description="На выполнение")
def activate(modeladmin, request, queryset):
    """Кастомное действие в админке - активация выбранных задач."""
    count = queryset.update(status=False, date_complite=None)
    modeladmin.message_user(request, f"Было обновлено {count} записей")


@admin.register(ToList)
class ToListAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "status",
        "name",
        "date_create",
        "date_complite",
        "slug",
    )
    list_editable = ("name",)

    ordering = ["status", "-name"]
    fields = ["name", "slug"]

    list_filter = ["status"]
    search_fields = (
        "name",
        "id",
    )

    prepopulated_fields = {"slug": ["name"]}
    actions = [activate, deactivate]
