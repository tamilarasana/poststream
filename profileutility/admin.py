from django.contrib import admin
from . import models

class ProfileAddressInline(admin.TabularInline):
    model = models.ProfileAddress
    
class ProfileFbtokenInline(admin.TabularInline):
    model = models.ProfileFbtoken

class ProfileNoticationPreferenceInline(admin.TabularInline):
    model = models.ProfileNoticationPreference

class ProfileAoiInline(admin.TabularInline):
    model = models.ProfileAoi

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['phone', 'gender', 'user']
    inlines = [ProfileAddressInline, ProfileFbtokenInline, ProfileNoticationPreferenceInline, ProfileAoiInline]

@admin.register(models.Enquirylog)
class EnquirylogAdmin(admin.ModelAdmin):
    list_display = ['type_of_enq', 'title', 'list', 'detail', 'mobile', 'email', 'remarks', 'kmdriven', 'price', 'enquire_at', 'scheduled',]
    search_fields = ['type_of_enq']

@admin.register(models.Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['profile', 'item']
    search_fields = ['item']    


@admin.register(models.ProfileActivity)
class ProfileActivityAdmin(admin.ModelAdmin):
    list_display = ['profile', 'type', 'instance']
    search_fields = ['type', 'instance']    


@admin.register(models.PaymentRequest)
class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ['internal_profile', 'phone', 'name', 'amount']
    search_fields = ['internal_profile', 'category', 'item']  


@admin.register(models.PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_reference_no', 'transaction_status', 'mode_of_payment', 'transaction_date', 'transaction_charge', 'total_amount_received', 'remarks']
    search_fields = ['transaction_reference_no', 'transaction_status', 'mode_of_payment', 'transaction_date']  

