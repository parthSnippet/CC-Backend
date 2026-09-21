from django.db import models


class Technology(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    category = models.CharField(max_length=100)

    short_description = models.CharField(
        max_length=300,
        blank=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="technologies/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title