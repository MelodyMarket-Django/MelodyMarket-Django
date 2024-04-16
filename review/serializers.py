from rest_framework import serializers
from .models import ReviewLike, Song

class ReviewLikeSerializer(serializers.ModelSerializer):
    user_likes_review = serializers.SerializerMethodField()
    song_average_rating = serializers.SerializerMethodField()

class Meta:
    model = ReviewLike
    fields = ['id', 'user', 'review', 'user_likes_review','song_average_rating']

    def get_user_likes_review(self, obj):
        user = self.context['request'].user
        return obj.review.likes.filter(id=user.id).exists() if user.is_authenticated else False


    def get_song_average_rating(self, obj):
        song = obj.review.song
        return song.average_rating() if song else None
