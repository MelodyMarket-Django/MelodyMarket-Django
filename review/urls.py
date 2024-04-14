
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
