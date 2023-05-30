from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("Frontp", views.FrontP, name="index"),
    path("Home", views.Home, name = "Home")
]