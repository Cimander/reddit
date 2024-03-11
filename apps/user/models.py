from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .manages import CustomUserManager



class MyUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    subscribe = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email





class User(MyUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    second_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    card_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email
