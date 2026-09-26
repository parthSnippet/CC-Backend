
from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "parent",
        "slug",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "tagline",
        "short_description",
        "description",
        "meta_title",
        "meta_description",
        "seo_keywords",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "parent",
                    "title",
                    "slug",
                    "tagline",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Service Details",
            {
                "fields": (
                    "highlights",
                    "deliverables",
                    "use_cases",
                )
            },
        ),
        (
            "SEO & Page Content",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "seo_keywords",
                    "page_h1",
                    "page_h2",
                    "image_alt_text",
                ),
                "description": (
                    "Manage search engine metadata and the main "
                    "headings displayed on this service page."
                ),
            },
        ),
        (
            "Media",
            {
                "fields": (
                    "image",
                    "icon",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )