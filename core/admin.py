from django.contrib import admin
from .models import SiteSetting, SocialLink, FooterMenu


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "phone",
        "email",
        "updated_at",
    )

    search_fields = (
        "company_name",
        "email",
        "phone",
        "address",
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        "platform",
        "url",
        "is_active",
        "sort_order",
    )

    list_filter = (
        "platform",
        "is_active",
    )

    search_fields = (
        "platform",
        "url",
    )

    ordering = (
        "sort_order",
        "platform",
    )


@admin.register(FooterMenu)
class FooterMenuAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "label",
        "url",
        "is_active",
        "sort_order",
    )

    list_filter = (
        "title",
        "is_active",
    )

    search_fields = (
        "title",
        "label",
        "url",
    )

    ordering = (
        "sort_order",
        "title",
    )