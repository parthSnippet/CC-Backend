from rest_framework import serializers

from .models import ComradeAIQuery


class ComradeAIQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComradeAIQuery
        fields = [
            "id",
            "query",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]