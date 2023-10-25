from django.db import models
from django.conf import settings

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=30)
    service_area = models.CharField(max_length=40)
    service_area_to = models.CharField(max_length=40, null=True)
    rent_price = models.IntegerField()
    image_url = models.CharField(max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    bookingDate = models.DateField(auto_now_add=True)
