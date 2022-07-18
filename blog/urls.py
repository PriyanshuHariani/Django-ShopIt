from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="BlogIndex"),
    path("trial/", views.trial, name="trial")
]