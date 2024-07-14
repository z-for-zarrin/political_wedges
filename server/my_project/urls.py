from .views import parallelogram_view, home_view
from django.urls import path

urlpatterns = [
    path("", home_view, name="home"),
    path("generate-graph/", parallelogram_view),
]
