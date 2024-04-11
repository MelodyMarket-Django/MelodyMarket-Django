from rest_framework import serializers
from .models import Playlist, Song, PlaylistSong
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "artist", "duration"]


class PlaylistSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)

    class Meta:
        model = PlaylistSong
        fields = ["id", "song"]


class PlaylistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    songs = PlaylistSongSerializer(many=True, read_only=True, source="playlistsong_set")

    class Meta:
        model = Playlist
        fields = ["id", "user", "name", "creation_date", "songs"]
