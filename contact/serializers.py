from rest_framework import serializers

from .models import ContactLead


class ContactLeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactLead

        fields = [
            "id",
            "name",
            "email",
            "company",
            "phone",
            "project_type",
            "budget",
            "timeline",
            "project_brief",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "created_at",
            "updated_at",
        ]