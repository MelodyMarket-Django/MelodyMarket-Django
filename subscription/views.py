from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        try:
            subscription = Subscription.objects.get(user=request.user)
            
            if not subscription.active:
                subscription.active = True
                subscription.save()

                request.user.isSubscribed = True
                request.user.save()

                serializer = self.get_serializer(subscription)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "이미 구독 중입니다."}, status=status.HTTP_400_BAD_REQUEST)
            
        except Subscription.DoesNotExist:
            subscription = Subscription.objects.create(user=request.user, active=True)

            request.user.isSubscribed = True
            request.user.save()
            
            serializer = self.get_serializer(subscription)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("You do not have permission to access this subscription.")
        serializer = self.get_serializer(instance)
        return Response(serializer.data)    



    


       