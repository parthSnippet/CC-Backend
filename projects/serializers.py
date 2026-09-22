from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    services = serializers.StringRelatedField(many=True)
    industries = serializers.StringRelatedField(many=True)
    technologies = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project

        fields = [
            "id",
            "project_number",
            "title",
            "category",
            "slug",
            "short_description",
            "description",
            "client_name",
            "project_url",
            "featured_image",
            "services",
            "industries",
            "technologies",
            "is_featured",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]