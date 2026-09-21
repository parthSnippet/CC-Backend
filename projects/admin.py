from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "client_name",
        "is_featured",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_featured",
        "is_active",
        "services",
        "industries",
        "technologies",
    )

    search_fields = (
        "title",
        "client_name",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "services",
        "industries",
        "technologies",
    )