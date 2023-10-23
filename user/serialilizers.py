from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserSerializer, UserSerializer as BasedUserSerializer
from .models import User


class UserCreateSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'password', 'is_owner']


class UserSerializer(BasedUserSerializer):
    class Meta(BasedUserSerializer.Meta):
        fields = ['id', 'email', 'is_owner']

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['id', 'email', 'password', 'is_owner']


#     def validate_user_id(self,user_id):
#         if not User.objects.filter(pk=user_id).exists():
#             return serializers.ValidationError("user id is invalid !")
#         return user_id
