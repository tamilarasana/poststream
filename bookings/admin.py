from .models import *
from import_export.admin import ImportExportModelAdmin



# Register your models here.


@admin.register(AppBooking)
class AppBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['profile', 'itemlist', 'created_at',
                    'payment_status', 'payment_id', 'amount']

@admin.register(NewCarBooking)
class NewCarBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'profile', 'address', 'item_description',
                    'booking_id', 'city', 'outlets', 'item_price', 'employee_id', 'referred_by', 'booking_status']

@admin.register(UsedCarBooking)
class UsedCarBookingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['itemlist', 'item_desc_id', 'booking_id', 'profile', 'address', 'brand', 'model', 'transmission', 'fuel', 'year', 'phone', 'email',
                    'kms_driven_starting', 'kms_driven_ending', 'price', 'lat', 'long', 'enquire_at', 'scheduled', 'employee_id', 'referred_by', 'booking_status']
                    
@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['booking_id', 'itemlist', 'item_desc_id', 'profile', 'address', 'name', 'email', 'mobile', 'city', 'outlet',
                    'model', 'varient', 'color', 'pickup_slot', 'item_price', 'employee_id', 'referred_id', 'deliverred_time', 'booking_status']