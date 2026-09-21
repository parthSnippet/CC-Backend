from django.contrib import admin
from .models import Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "slug",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "title",
        "category",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }