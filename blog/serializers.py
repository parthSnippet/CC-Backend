from rest_framework import serializers

from .models import BlogCategory, BlogPost


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name",
            "slug",
            "is_active",
            "created_at",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "excerpt",
            "content",
            "featured_image",
            "author",
            "is_published",
            "published_at",
            "created_at",
            "updated_at",
        ]