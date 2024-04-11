<<<<<<< HEAD

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView, SignUpView
from django.contrib.auth import views as auth_views

# main
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet) 

urlpatterns = [
# API 경로
    path('api/', include(router.urls)), 
    
    path('reviews/', ReviewListView.as_view(), name='review-list'),  # 리스트 뷰
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),  # 리뷰 상세 정보 뷰
    path('reviews/new/', ReviewCreateView.as_view(), name='review-create'),  # 리뷰 생성 뷰
    path('reviews/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review-edit'),  # 리뷰 수정 뷰
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),  # 리뷰 삭제 뷰
    
    # 사용자 인증 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    
    # 회원가입 
    path('signup/', SignUpView.as_view(), name='signup'),  
]
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from django.contrib.auth import views as auth_views
from .views import (
    AlbumViewSet, ReviewViewSet, AlbumReviewsViewSet, 
    ReviewListView, ReviewDetailView, 
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView, 
    SignUpView, AlbumListView, AlbumDetailView
)

# 메인 
router = DefaultRouter()
router.register(r'albums', AlbumViewSet)  # 앨범 관련 라우터
router.register(r'reviews', ReviewViewSet)  # 리뷰 관련 라우터

# 앨범별 리뷰를 위한 
albums_router = NestedSimpleRouter(router, r'albums', lookup='album')
albums_router.register(r'reviews', AlbumReviewsViewSet, basename='album-reviews')

urlpatterns = [
    # API 경로
    path('api/', include(router.urls)),
    path('api/', include(albums_router.urls)),  # 중첩된 라우터를 'api/' 경로에 포함
    
    # 리뷰 CRUD 경로
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/new/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review-edit'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    
    # 사용자 인증 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # 앨범 리스트 및 상세 정보 
    path('albums-list/', AlbumListView.as_view(), name='album-list'),
    path('albums-detail/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    
    # 회원가입 
    path('signup/', SignUpView.as_view(), name='signup'),
]



>>>>>>> 5209a3d (🔧 crud 파일추가- 초안)
