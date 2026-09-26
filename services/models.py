
# from django.db import models


# class Service(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)

#     tagline = models.CharField(
#         max_length=200,
#         blank=True,
#         null=True
#     )

#     short_description = models.CharField(max_length=300)
#     description = models.TextField()

#     highlights = models.JSONField(
#         default=list,
#         blank=True
#     )

#     deliverables = models.JSONField(
#         default=list,
#         blank=True
#     )

#     use_cases = models.JSONField(
#         default=list,
#         blank=True
#     )

#     image = models.ImageField(
#         upload_to="services/",
#         blank=True,
#         null=True
#     )

#     icon = models.CharField(
#         max_length=100,
#         blank=True,
#         null=True
#     )

#     parent = models.ForeignKey(
#         "self",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="sub_services"
#     )

#     is_active = models.BooleanField(default=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["-created_at"]

#     def __str__(self):
#         return self.title


# class ServiceVideo(models.Model):
#     VIDEO_TYPE_CHOICES = [
#         ("mp4", "MP4 Video"),
#         ("youtube", "YouTube Video"),
#     ]

#     service = models.ForeignKey(
#         Service,
#         on_delete=models.CASCADE,
#         related_name="videos",
#     )

#     video_type = models.CharField(
#         max_length=20,
#         choices=VIDEO_TYPE_CHOICES,
#         default="mp4",
#     )

#     video_file = models.FileField(
#         upload_to="services/videos/",
#         blank=True,
#         null=True,
#     )

#     youtube_url = models.URLField(
#         blank=True,
#         null=True,
#     )

#     thumbnail = models.ImageField(
#         upload_to="services/video-thumbnails/",
#         blank=True,
#         null=True,
#     )

#     is_active = models.BooleanField(default=True)

#     sort_order = models.PositiveIntegerField(default=0)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["sort_order", "-created_at"]

#     def __str__(self):
#         return f"{self.service.title} - {self.get_video_type_display()}"



from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    tagline = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    short_description = models.CharField(max_length=300)
    description = models.TextField()

    highlights = models.JSONField(
        default=list,
        blank=True
    )

    deliverables = models.JSONField(
        default=list,
        blank=True
    )

    use_cases = models.JSONField(
        default=list,
        blank=True
    )

    # SEO Fields
    meta_title = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    meta_description = models.CharField(
        max_length=320,
        blank=True,
        default=""
    )

    seo_keywords = models.TextField(
        blank=True,
        default=""
    )

    page_h1 = models.CharField(
        max_length=250,
        blank=True,
        default=""
    )

    page_h2 = models.CharField(
        max_length=250,
        blank=True,
        default=""
    )

    image_alt_text = models.CharField(
        max_length=250,
        blank=True,
        default=""
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sub_services"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ServiceVideo(models.Model):
    VIDEO_TYPE_CHOICES = [
        ("mp4", "MP4 Video"),
        ("youtube", "YouTube Video"),
    ]

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="videos",
    )

    video_type = models.CharField(
        max_length=20,
        choices=VIDEO_TYPE_CHOICES,
        default="mp4",
    )

    video_file = models.FileField(
        upload_to="services/videos/",
        blank=True,
        null=True,
    )

    youtube_url = models.URLField(
        blank=True,
        null=True,
    )

    thumbnail = models.ImageField(
        upload_to="services/video-thumbnails/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return f"{self.service.title} - {self.get_video_type_display()}"