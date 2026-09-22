from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/",include("services.urls")),
    path("api/v1/",include("industries.urls")),
    path("api/v1/",include("technologies.urls")),
    path("api/v1/",include("projects.urls")),
    path("api/v1/",include("blog.urls")),
    path("api/v1/",include("contact.urls")),
    path("api/v1/",include("core.urls")),
    path("api/v1/", include("about.urls")),
    path("api/v1/", include("comrade_ai.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )