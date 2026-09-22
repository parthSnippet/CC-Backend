from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "project_number",
        "title",
        "category",
        "client_name",
        "is_featured",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
        "services",
        "industries",
        "technologies",
    )

    search_fields = (
        "project_number",
        "title",
        "category",
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

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "project_number",
                    "title",
                    "category",
                    "slug",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Project Details",
            {
                "fields": (
                    "client_name",
                    "project_url",
                    "featured_image",
                )
            },
        ),
        (
            "Relations",
            {
                "fields": (
                    "services",
                    "industries",
                    "technologies",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_featured",
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )