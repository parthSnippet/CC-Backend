from django.contrib import admin

from .models import Industry


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
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
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "tagline",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Industry Details",
            {
                "fields": (
                    "challenges",
                    "solutions",
                    "use_cases",
                )
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