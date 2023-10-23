from django.contrib import admin
from .models import Car, Booking

# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    '''Admin View for Car'''

    list_display = ('id', 'name', 'brand', 'service_area',
                    'rent_price', 'image_url', 'owner')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    '''Admin View for Booking'''

    list_display = ('id','user','car','bookingDate')
    