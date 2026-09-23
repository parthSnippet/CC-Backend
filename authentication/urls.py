from django.urls import path

from .views import (
    AdminLoginView,
    AdminMeView,
    AdminTokenRefreshView,
)


urlpatterns = [
    path(
        "login/",
        AdminLoginView.as_view(),
        name="admin-login",
    ),
    path(
        "refresh/",
        AdminTokenRefreshView.as_view(),
        name="admin-token-refresh",
    ),
    path(
        "me/",
        AdminMeView.as_view(),
        name="admin-me",
    ),
]