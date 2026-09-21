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

    list_filter = ("is_active",)

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }