from django.contrib.auth.models import User
from django.db import models

class Genre(models.Model):
    # 음악 장르
    name = models.CharField(max_length=100)

class Song(models.Model):
    # 노래 정보를 저장하는
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name='songs')
    cover_image = models.ImageField(upload_to="song_covers/", blank=True)
    release_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_songs')

    def __str__(self):
        return self.title

class Review(models.Model):
    # 사용자가 작성한 리뷰를 저장하는
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserRecommendation(models.Model):
    # 사용자가 다른 사용자에게 음악을 추천할 때 사용하는 모델
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    reason = models.TextField()
