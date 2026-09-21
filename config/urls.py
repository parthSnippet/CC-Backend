from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/",
        include("services.urls")
    ),

     path(
        "api/",
        include("industries.urls")
    ),

    path(
    "api/",
    include("technologies.urls")
    ),

    path(
    "api/",
    include("projects.urls")
    ),

    path(
    "api/",
    include("blog.urls")
    ),

    path(
    "api/",
    include("contact.urls")
    ),

    
    path(
    "api/",
    include("core.urls")
    ),
]