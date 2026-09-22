from rest_framework import serializers

from .models import AboutPage


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = [
            "id",
            "projects_delivered",
            "happy_clients",
            "years_experience",
            "tech_experts",
            "how_we_work_title",
            "how_we_work_description",
            "how_we_work_points",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "updated_at",
        ]