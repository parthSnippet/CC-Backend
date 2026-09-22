from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service

        fields = [
            "id",
            "title",
            "slug",
            "tagline",
            "short_description",
            "description",
            "highlights",
            "deliverables",
            "use_cases",
            "image",
            "icon",
            "is_active",
            "created_at",
            "updated_at",
        ]