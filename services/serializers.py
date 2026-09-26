# from rest_framework import serializers

# from .models import Service, ServiceVideo


# class ServiceVideoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ServiceVideo

#         fields = [
#             "id",
#             "service",
#             "video_type",
#             "video_file",
#             "youtube_url",
#             "thumbnail",
#             "is_active",
#             "sort_order",
#             "created_at",
#             "updated_at",
#         ]


# class ServiceSerializer(serializers.ModelSerializer):

#     videos = ServiceVideoSerializer(many=True, read_only=True)
#     sub_services = serializers.SerializerMethodField()

#     def get_sub_services(self, obj):
#         qs = obj.sub_services.filter(is_active=True)
#         return ServiceSerializer(qs, many=True, context=self.context).data

#     class Meta:
#         model = Service

#         fields = [
#             "id",
#             "parent",
#             "title",
#             "slug",
#             "tagline",
#             "short_description",
#             "description",
#             "highlights",
#             "deliverables",
#             "use_cases",
#             "image",
#             "icon",
#             "is_active",
#             "created_at",
#             "updated_at",
#             "videos",
#             "sub_services",
#         ]



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
    sub_services = serializers.SerializerMethodField()

    def get_sub_services(self, obj):
        qs = obj.sub_services.filter(is_active=True)
        return ServiceSerializer(
            qs,
            many=True,
            context=self.context
        ).data

    class Meta:
        model = Service

        fields = [
            "id",
            "parent",
            "title",
            "slug",
            "tagline",
            "short_description",
            "description",
            "highlights",
            "deliverables",
            "use_cases",

            # SEO Fields
            "meta_title",
            "meta_description",
            "seo_keywords",
            "page_h1",
            "page_h2",
            "image_alt_text",

            # Media and other fields
            "image",
            "icon",
            "is_active",
            "created_at",
            "updated_at",
            "videos",
            "sub_services",
        ]