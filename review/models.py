from django.contrib.auth.models import User
from django.db import models


class Song(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    duration = models.FloatField()

    def str(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.CharField(max_length=100, null=True, blank=True)
    ating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class UserRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(song, on_delete=models.CASCADE)
    reason = models.TextField()

