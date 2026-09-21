from rest_framework import serializers
from .models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "short_description",
            "icon",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]