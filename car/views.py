from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CarSerializer, BookingSerializer, CreateBookingSerializer, UserCarSerializer
from .models import Booking, Car
from .paginations import DefaultPagination

# Create your views here.


class CarViewSet(ModelViewSet):
    queryset = Car.objects.select_related('owner').all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['service_area']
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in ['PUT', 'POST', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


class UserCarViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserCarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(owner_id=self.request.user.id)


class BookingViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateBookingSerializer
        return BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user_id=self.request.user.id).select_related('car').select_related('user')

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
