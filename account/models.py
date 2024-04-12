from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, blank=True, null=True)
    birthDate = models.DateField()
    provider = models.CharField(max_length=255, blank=True, null=True)
    accountId = models.CharField(max_length=255, blank=True, null=True)
    isSubscribed = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username


