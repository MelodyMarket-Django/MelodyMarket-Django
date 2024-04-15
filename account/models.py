from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

class User(AbstractBaseUser):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, blank=True, null=True)
    birthDate = models.DateField(null=True, blank=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    accountId = models.CharField(max_length=255, blank=True, null=True)
    isSubscribed = models.BooleanField(default=False)
    objects = CustomUserManager()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True

