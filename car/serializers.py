from rest_framework import serializers
from .models import Car, Booking
from user.models import User
from user.serialilizers import UserCreateSerializer
from datetime import datetime


class CarSerializer(serializers.ModelSerializer):

    owner = UserCreateSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'name', 'brand',
                  'service_area', 'service_area_to', 'rent_price', 'image_url', 'owner']

    def create(self, validated_data):
        name = self.validated_data['name']
        brand = self.validated_data['brand']
        service_area = self.validated_data['service_area']
        service_area_to = self.validated_data['service_area_to']
        rent_price = self.validated_data['rent_price']
        image_url = self.validated_data['image_url']

        user_id = self.context.get('user_id')

        if User.objects.filter(pk=user_id).exists():
            if User.objects.get(pk=user_id).is_owner:
                return Car.objects.create(name=name, brand=brand, service_area=service_area, service_area_to=service_area_to, rent_price=rent_price, image_url=image_url, owner_id=user_id)

            else:
                raise serializers.ValidationError(
                    {'error': 'only owner can be add car'})
        else:
            raise serializers.ValidationError(
                {'error': 'Wrong user Cradintial'})


class UserCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'name', 'brand',
                  'service_area', 'service_area_to', 'rent_price', 'image_url', 'owner']


class BookingSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)
    car = CarSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'car', 'phone', 'bookingDate']


class CreateBookingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    car_id = serializers.IntegerField()

    class Meta:
        model = Booking
        fields = ['id', 'user_id', 'car_id', 'phone', 'bookingDate']

    def validate_car_id(self, car_id):
        if Car.objects.filter(pk=car_id).exists():
            return car_id
        raise serializers.ValidationError({'error': 'car id not valid !'})

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        car_id = self.validated_data['car_id']
        phone = self.validated_data['phone']
        print(datetime.today().date())
        if User.objects.filter(pk=user_id).exists():
            today = datetime.today().date()
            if not Booking.objects.filter(
                    user_id=user_id, car_id=car_id, bookingDate=today).exists():

                return Booking.objects.create(user_id=user_id, phone=phone, car_id=car_id)
            raise serializers.ValidationError(
                {'error': 'You all ready Booked This car Today !'})
        raise serializers.ValidationError({'error': 'User Not Valid !'})
