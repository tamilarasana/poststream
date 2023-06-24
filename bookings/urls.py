from unicodedata import name
from unittest.mock import patch
from django.urls import path
from .views import *
app_name = "SuperApp"

urlpatterns = [
    path("create_fetch_appbooking/", appBooking),
    path("get_update_delete_appbooking/<int:id>", appBookingUD),

    path("create_fetch_newcarbooking/", newCarBooking),
    path("get_update_delete_newcarbooking/<int:id>", newCarBookingUD),

    path("create_fetch_usedcarbooking/", usedCarBooking),
    path("get_update_delete_usedcarbooking/<int:id>", usedCarBookingUD),

    path("create_fetch_servicebooking/", serviceBooking),
    path("get_update_delete_servicebooking/<int:id>", serviceBookingUD),
    

]