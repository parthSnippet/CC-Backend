from django.db import models


class SiteSetting(models.Model):
    company_name = models.CharField(
        max_length=200,
        default="Comerade Coders"
    )

    tagline = models.CharField(
        max_length=300,
        default="Technology That Moves Business Forward."
    )

    description = models.TextField(
        blank=True
    )

    logo = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    favicon = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    copyright_text = models.CharField(
        max_length=300,
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.company_name


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("linkedin", "LinkedIn"),
        ("youtube", "YouTube"),
        ("twitter", "Twitter"),
        ("github", "GitHub"),
    ]

    platform = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES
    )

    url = models.URLField()

    is_active = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "platform"]

    def __str__(self):
        return self.platform

class FooterMenu(models.Model):
    title = models.CharField(
        max_length=100
    )

    label = models.CharField(
        max_length=100
    )

    url = models.CharField(
        max_length=300
    )

    is_active = models.BooleanField(
        default=True
    )

    sort_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["sort_order", "title"]

    def __str__(self):
        return f"{self.title} - {self.label}"