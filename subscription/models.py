from django.db import models
from django.conf import settings

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    price = models.FloatField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Subscription"