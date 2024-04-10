from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")
    name = models.CharField(max_length=255)
    creation_date = models.DateField()


class Song(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    duration = models.FloatField()
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="songs")


class PlaylistSong(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE, related_name="playlist_songs"
    )
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name="playlist_songs"
    )
    order = models.IntegerField()


class Album(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField()
    description = models.TextField()
