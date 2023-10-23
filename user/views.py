from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serialilizers import UserCreateSerializer
from .models import User
# Create your views here.


# class UserViewSet(ModelViewSet):

#     serializer_class = UserSerializer

#     # def get_permissions(self):
#     #     if self.request.method == 'GET':
#     #         return [IsAuthenticated()]
#     #     elif self.request.method in ['PUT', 'DELETE']:
#     #         return [IsAdminUser()]
#     #     return [AllowAny()]

#     def get_queryset(self):
#         user = self.request.user
#         return User.objects.filter(id=user.id)

#     def get_serializer_context(self):
#         return {"user_id": self.request.user.id}
