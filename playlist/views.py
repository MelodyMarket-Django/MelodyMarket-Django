from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated  # 주석 해제
from django.shortcuts import get_object_or_404
from .models import Playlist, Song
from .serializers import PlaylistSerializer, SongSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]  # 모든 액션에 대해 인증된 사용자만 접근 가능

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=request.user
        )  # 현재 요청을 보낸 사용자를 Playlist 객체의 user 필드에 할당
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def list(self, request, *args, **kwargs):
        # queryset = self.get_queryset().filter(user=request.user)  # 주석 처리
        queryset = self.get_queryset()  # 변경: 모든 사용자가 접근 가능
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]  # 모든 액션에 대해 인증된 사용자만 접근 가능

    @action(
        detail=True,
        methods=["post"],
        url_path="add_to_playlist",
        permission_classes=[IsAuthenticated],
    )
    def add_to_playlist(self, request, *args, **pk):
        song = self.get_object()
        playlist_id = request.data.get("playlist_id")
        playlist = get_object_or_404(Playlist, pk=playlist_id)
        # 여기서는 사용자 확인 로직을 제거하고 모든 인증된 사용자가 접근할 수 있도록 함
        playlist.songs.add(song)
        return Response(
            {"detail": "Song added to playlist successfully."},
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=["post"],
        url_path="remove_from_playlist",
        permission_classes=[IsAuthenticated],
    )
    def remove_from_playlist(self, request, *args, **pk):
        song = self.get_object()
        playlist_id = request.data.get("playlist_id")
        playlist = get_object_or_404(Playlist, pk=playlist_id)
        # 여기서는 사용자 확인 로직을 제거하고 모든 인증된 사용자가 접근할 수 있도록 함
        playlist.songs.remove(song)
        return Response(
            {"detail": "Song removed from playlist successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
