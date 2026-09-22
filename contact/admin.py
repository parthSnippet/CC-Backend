from django.contrib import admin

from .models import ContactLead


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "company",
        "project_type",
        "budget",
        "timeline",
        "status",
        "created_at",
    )

    list_filter = (
        "project_type",
        "budget",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "company",
        "phone",
        "project_brief",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Contact Information",
            {
                "fields": (
                    "name",
                    "email",
                    "company",
                    "phone",
                )
            },
        ),
        (
            "Project Information",
            {
                "fields": (
                    "project_type",
                    "budget",
                    "timeline",
                    "project_brief",
                )
            },
        ),
        (
            "Lead Status",
            {
                "fields": (
                    "status",
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