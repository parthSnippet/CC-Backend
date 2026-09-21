from django.contrib import admin
from .models import BlogCategory, BlogPost


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "author",
        "is_published",
        "published_at",
        "created_at",
    )

    list_filter = (
        "category",
        "is_published",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
        "author",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    autocomplete_fields = (
        "category",
    )