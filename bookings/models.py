from django.db import models
from profileutility.models import *
from showcase.models import *

# Create your models here.

class AppBooking(models.Model):
    COMPLETED = 'Completed'
    PENDING = 'Pending'
    ERROR = 'Error'
    DECLINED = 'Declined'

    STATUS_CHOICES = [
        (COMPLETED, 'Completed'),
        (PENDING, 'Pending'),
        (ERROR, 'Error'),
        (DECLINED, 'Declined')
    ]

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=PENDING)
    payment_id = models.CharField(
        max_length=250, blank=True, null=True, unique=True)
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'App Bookings'
        verbose_name_plural = 'App Bookings'

    # def __str__(self) -> str:
    #         return self.cust_id_or_reg_no

class NewCarBooking(models.Model):
    BOOKED = 'Booked'
    RETAIL = 'Retail'
    RETAILCANCEL = 'RetailCancel'
    DELIVERRED = 'Deliverred'

    STATUS_CHOICES = [
        (BOOKED, 'Booked'),
        (RETAIL, 'Retail'),
        (RETAILCANCEL, 'RetailCancel'),
        (DELIVERRED, 'Deliverred')
    ]
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    mobile = models.CharField(max_length=250, blank=True, null=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True, unique=True)

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)
    item_description = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    booking_id = models.ForeignKey(
        AppBooking, on_delete=models.CASCADE, blank=True, null=True)

    city = models.CharField(max_length=250, blank=True, null=True)
    outlets = models.CharField(max_length=250, blank=True, null=True)
    item_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=255, blank=True, null=True)

    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        verbose_name = 'NewCar Booking'
        verbose_name_plural = 'NewCar Booking'

    

class UsedCarBooking(models.Model):

    ENQUIRED = 'Enquired'
    CONTACTED = 'Contacted'
    BOOKED = 'Booked'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'
    CAR_NOT_AVAILABLE = 'Car not available'

    STATUS_CHOICES = [
        (ENQUIRED, 'Enquired'),
        (CONTACTED, 'Contacted'),
        (BOOKED, 'Booked'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled'),
        (CAR_NOT_AVAILABLE, 'Car not available')
    ]

    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    item_desc_id = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    booking_id = models.ForeignKey(
        AppBooking, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)

    brand = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=250, blank=True, null=True)
    transmission = models.CharField(max_length=250, blank=True, null=True)
    fuel = models.CharField(max_length=250, blank=True, null=True)
    year = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True, unique=True)
    kms_driven_starting = models.CharField(
        max_length=250, blank=True, null=True)
    kms_driven_ending = models.CharField(max_length=250, blank=True, null=True)
    price = models.CharField(max_length=250, blank=True, null=True)
    lat = models.CharField(max_length=250, blank=True, null=True)
    long = models.CharField(max_length=250, blank=True, null=True)
    enquire_at = models.DateTimeField(auto_now_add=True)
    scheduled = models.DateTimeField(auto_now=True, blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.CharField(max_length=255, blank=True, null=True)

    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=ENQUIRED)

    class Meta:
        verbose_name = 'UsedCar Booking'
        verbose_name_plural = 'UsedCar Booking'


class Service(models.Model):

    BOOKED = 'Booked'
    CONTACTED = 'Contacted'
    PICKED = 'Picked Up'
    DELIVERRED = 'Deliverred'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (BOOKED, 'Booked'),
        (CONTACTED, 'Contacted'),
        (PICKED, 'Picked Up'),
        (DELIVERRED, 'Deliverred'),
        (CANCELLED, 'Cancelled')
    ]

    booking_id = models.ForeignKey(
        AppBooking, on_delete=models.CASCADE, blank=True, null=True)
    itemlist = models.ForeignKey(
        Itemlist, on_delete=models.CASCADE, blank=True, null=True)
    item_desc_id = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    address = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    cust_id_or_reg_no = models.CharField(
        max_length=250, blank=True, null=True, unique=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    outlet = models.CharField(max_length=255, blank=True, null=True)

    model = models.CharField(max_length=255, blank=True, null=True)
    varient = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)

    pickup_slot = models.DateTimeField(auto_now=True)
    item_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True)

    employee_id = models.CharField(max_length=255, blank=True, null=True)
    referred_id = models.CharField(max_length=255, blank=True, null=True)

    deliverred_time = models.DateTimeField(blank=True, null=True)
    booking_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=BOOKED)

    class Meta:
        verbose_name = 'Service Booking'
        verbose_name_plural = 'Service Booking'
