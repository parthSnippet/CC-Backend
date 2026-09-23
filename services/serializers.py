from rest_framework import serializers

from .models import Service, ServiceVideo


class ServiceVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceVideo

        fields = [
            "id",
            "service",
            "video_type",
            "video_file",
            "youtube_url",
            "thumbnail",
            "is_active",
            "sort_order",
            "created_at",
            "updated_at",
        ]


class ServiceSerializer(serializers.ModelSerializer):

    videos = ServiceVideoSerializer(many=True, read_only=True)

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
            "videos",
        ]