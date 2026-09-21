from django.contrib import admin

from .models import ContactLead


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "company",
        "subject",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "company",
        "subject",
        "message",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )