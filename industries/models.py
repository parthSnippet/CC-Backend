from django.db import models


class Industry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    tagline = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    challenges = models.JSONField(
        default=list,
        blank=True
    )

    solutions = models.JSONField(
        default=list,
        blank=True
    )

    use_cases = models.JSONField(
        default=list,
        blank=True
    )

    image = models.ImageField(
        upload_to="industries/",
        blank=True,
        null=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title