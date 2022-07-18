from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("about", views.about, name="aboutUs"),
    path("contact", views.contact, name="contactUs"),
    path("tracker", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("prodView/", views.prodView, name="prodView"),
    path("checkout/", views.checkout, name="checkout")
]