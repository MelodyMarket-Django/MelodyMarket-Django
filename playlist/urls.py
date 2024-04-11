from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaylistViewSet, SongViewSet

router = DefaultRouter()

router.register(r"playlists", PlaylistViewSet)
router.register(r"songs", SongViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

# PlaylistViewSet 경로

#     플레이리스트 목록 조회 및 생성
#         GET /playlists/ : 모든 플레이리스트를 조회합니다.
#         POST /playlists/ : 새로운 플레이리스트를 생성합니다.

#     플레이리스트 세부 조회 및 수정
#         GET /playlists/{playlist_id}/ : 특정 플레이리스트의 세부 정보를 조회합니다.
#         PUT /playlists/{playlist_id}/ : 특정 플레이리스트를 전체적으로 수정합니다.
#         PATCH /playlists/{playlist_id}/ : 특정 플레이리스트를 부분적으로 수정합니다.
#         DELETE /playlists/{playlist_id}/ : 특정 플레이리스트를 삭제합니다.

# SongViewSet 경로

#     노래 목록 조회 및 생성
#         GET /songs/ : 모든 노래를 조회합니다.
#         POST /songs/ : 새로운 노래를 생성합니다.

#     노래 세부 조회 및 수정
#         GET /songs/{song_id}/ : 특정 노래의 세부 정보를 조회합니다.
#         PUT /songs/{song_id}/ : 특정 노래를 전체적으로 수정합니다.
#         PATCH /songs/{song_id}/ : 특정 노래를 부분적으로 수정합니다.
#         DELETE /songs/{song_id}/ : 특정 노래를 삭제합니다.

# @action으로 추가된 경로

#     플레이리스트에 노래 추가 및 제거
#         POST /songs/{song_id}/add_to_playlist/ : 특정 노래를 플레이리스트에 추가합니다.
#         POST /songs/{song_id}/remove_from_playlist/ : 특정 노래를 플레이리스트에서 제거합니다.
