from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, is_owner):
        if not email:
            raise ValueError('please give and email !')
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, is_owner=is_owner)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        superuser = self.create_user(
            email=email, password=password, is_owner=True)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self.db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = "email"
