from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, SubscriptionDetail

router = DefaultRouter()
router.register('', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detail/', SubscriptionDetail.as_view(), name='subscription_detail'),
]