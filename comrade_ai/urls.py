from django.urls import path

from .views import ComradeAIQueryListCreateView


urlpatterns = [
    path(
        "comrade-ai/",
        ComradeAIQueryListCreateView.as_view(),
        name="comrade-ai-query",
    ),
]