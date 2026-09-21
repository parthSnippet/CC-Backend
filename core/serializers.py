from rest_framework import serializers

from .models import SiteSetting, SocialLink, FooterMenu


class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = [
            "id",
            "company_name",
            "tagline",
            "description",
            "logo",
            "favicon",
            "phone",
            "email",
            "address",
            "copyright_text",
            "updated_at",
        ]


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = [
            "id",
            "platform",
            "url",
            "is_active",
            "sort_order",
        ]


class FooterMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterMenu
        fields = [
            "id",
            "title",
            "label",
            "url",
            "is_active",
            "sort_order",
        ]