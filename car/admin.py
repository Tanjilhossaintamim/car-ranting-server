from django.contrib import admin
from .models import Car, Booking

# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    '''Admin View for Car'''

    list_display = ('id', 'name', 'brand', 'service_area','service_area_to',
                    'rent_price', 'image_url', 'owner')
    list_per_page=10

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    '''Admin View for Booking'''

    list_display = ('id','user','car','phone','bookingDate')
    list_per_page=10
    