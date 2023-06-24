from rest_framework import serializers
from.models import *


class AppBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppBooking
        fields = '__all__' 


class NewCarBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewCarBooking
        fields = '__all__'


class UsedCarBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsedCarBooking
        fields = '__all__'


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
