from rest_framework import routers
# from user.views import UserViewSet
from car.views import BookingViewSet, CarViewSet, UserCarViewSet


router = routers.DefaultRouter()
router.register('cars', CarViewSet, basename='car')
router.register('usercars', UserCarViewSet, basename='usercar')
router.register('booking', BookingViewSet, basename='booking')
urlpatterns = router.urls
