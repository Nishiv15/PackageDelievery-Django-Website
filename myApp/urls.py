from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("loading", views.processing, name="loading"),
]