from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("chirpstack", views.chirpstack_callback_view, name="chirpstack"),
    path("meter/<int:pk>", views.meter_profile_view, name="meter"),
]