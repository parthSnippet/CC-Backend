from rest_framework import serializers
from .models import Industry


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "description",
            "image",
            "icon",
            "is_active",
            "created_at",
            "updated_at",
        ]