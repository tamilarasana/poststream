from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from showcase.models import ItemDescription
from showcase.models import Category


class Profile(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    ACTIVE = 'Active'
    INACTIVE = 'Inactive'

    ACTIVE_STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    phone = models.CharField(max_length=255, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    year_of_birth = models.IntegerField(null=True, blank=True)
    active_status = models.CharField(
        max_length=50, choices=ACTIVE_STATUS, default=ACTIVE)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name='user')
        
    def __str__(self) -> str:
         return self.user.username

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'


class ProfileAddress(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_address')
    type_of_address = models.CharField(max_length=255, null=True, blank=True)
    door_no = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=255, null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1, null=True, blank=True)
    class Meta:
        verbose_name = 'Profile Address'
        verbose_name_plural = 'Profile Address'

    def __str__(self) -> str:
         return self.city


class ProfileFbtoken(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_fb')
    type_of_token = models.CharField(max_length=255, null=True, blank=True)
    device_name = models.CharField(max_length=255, null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1, null=True, blank=True)
    class Meta:
        verbose_name = 'FB Tokens'
        verbose_name_plural = 'FB Tokens'


class ProfileNoticationPreference(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='profile_preference')
    type_of_notification = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1, null=True, blank=True)
    class Meta:
        verbose_name = 'Notification Preference'
        verbose_name_plural = 'Notification Preferences'
      
      
class ProfileAoi(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='profile_aoi')
    type = models.CharField(max_length=255, null=True, blank=True)
    interest = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = 'Profile AOI'
        verbose_name_plural = 'Profile AOI'


class ProfileSearch(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='profile_search', default=None)
    keyword = models.CharField(max_length=255)
    search_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Profile Search'
        verbose_name_plural = 'Profile Search'


class ProfileActivity(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='activity_profile')
    type = models.CharField(max_length=255, null=True, blank=True)
    instance = models.CharField(max_length=255, null=True, blank=True)
    search_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Profile Analytics'
        verbose_name_plural = 'Profile Analytics'


class Enquirylog(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_log')
    profile_address = models.ForeignKey(
        ProfileAddress, on_delete=models.CASCADE, related_name='profile_address')
    
    type_of_enq = models.CharField(max_length=255, null=True, blank=True) 
    title = models.CharField(max_length=255, null=True, blank=True) 
    list = models.CharField(max_length=255, null=True, blank=True)
    detail = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    remarks = models.TextField(null=True, blank=True)
    kmdriven = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)

    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)

    enquire_at = models.DateTimeField(auto_now=True, null= True, blank=True)
    scheduled = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Enquiry Log'
        verbose_name_plural = 'Enquiry Logs'


class Wishlist(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='wishlist_profile')
    item = models.ForeignKey(
        ItemDescription, on_delete=models.CASCADE, related_name='profile_item')

    class Meta:
        unique_together = [['profile', 'item']]
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'


class PaymentRequest(models.Model):
    COMPLETED = 'Completed'
    PENDING = 'Pending'
    EXPIRED = 'Expired'
    DECLINED = 'Declined'

    STATUS_CHOICES = [
        (COMPLETED, 'Completed'),
        (PENDING, 'Pending'),
        (EXPIRED, 'Expired'),
        (DECLINED, 'Declined')
    ]


    internal_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile_crm', null=True, blank=True)
    # cust_id = models.CharField(max_length=255, null=True, blank=True)
    register_no = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=PENDING)
   
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, related_name='crm_category', null=True, blank=True)
    # item = models.ForeignKey(
    #     ItemDescription, on_delete=models.CASCADE, related_name='crm_item', null=True, blank=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)

    transaction_number = models.CharField(max_length=255, null=True, blank=True)

    requested_employee_id = models.CharField(max_length=255, null=True, blank=True)
    requested_employee_name = models.CharField(max_length=255, null=True, blank=True)
    requested_employee_mobile = models.CharField(max_length=255, null=True, blank=True)
    requested_employee_location = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    channel = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    dont_show = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Payment Request'
        verbose_name_plural = 'Payment Requests'


class PaymentTransaction(models.Model):
    COMPLETED = 'Completed'
    PENDING = 'Pending'
    EXPIRED = 'Expired'

    STATUS_CHOICES = [
        (COMPLETED, 'Completed'),
        (PENDING, 'Pending'),
        (EXPIRED, 'Expired'),
    ]

    crm_profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name='crm_profile', null=True, blank=True)
    payment_instance = models.ForeignKey(
        PaymentRequest, on_delete=models.PROTECT, related_name='payment_transaction', null=True, blank=True)
    
    transaction_reference_no = models.CharField(max_length=255, null=True, blank=True)
    transaction_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    mode_of_payment = models.CharField(max_length=255, null=True, blank=True)
    transaction_date = models.DateTimeField(null=True, blank=True)
    transaction_charge = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    total_amount_received = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Payment Transaction'
        verbose_name_plural = 'Payment Transactions'




