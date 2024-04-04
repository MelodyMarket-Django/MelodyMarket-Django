from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateField()
    price = models.FloatField()

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=100)
    paymentDate = models.DateField()
