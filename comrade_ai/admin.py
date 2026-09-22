from django.contrib import admin

from .models import ComradeAIQuery


@admin.register(ComradeAIQuery)
class ComradeAIQueryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "query_preview",
        "created_at",
    )

    list_display_links = (
        "id",
        "query_preview",
    )

    search_fields = (
        "query",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

    @admin.display(description="Query")
    def query_preview(self, obj):
        return obj.query[:100]