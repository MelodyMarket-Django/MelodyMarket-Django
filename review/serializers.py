from rest_framework import serializers
from .models import song, Review

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'  # 모든 필드를 포함하거나, 필요한 필드만 명시적으로 나열

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
