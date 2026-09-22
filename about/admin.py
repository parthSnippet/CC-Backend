from django.contrib import admin

from .models import AboutPage


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = (
        "projects_delivered",
        "happy_clients",
        "years_experience",
        "tech_experts",
        "updated_at",
    )

    readonly_fields = (
        "updated_at",
    )