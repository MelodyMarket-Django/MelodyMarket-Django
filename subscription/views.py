from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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
                serializer = self.get_serializer(subscription)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "이미 구독 중입니다."}, status=status.HTTP_400_BAD_REQUEST)
            
        except Subscription.DoesNotExist:
            subscription = Subscription.objects.create(user=request.user, active=True)
            serializer = self.get_serializer(subscription)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class SubscriptionDetail(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        try: 
            subsription = Subscription.objects.get(user=self.request.user)
            return subsription
        except Subscription.DoesNotExist:
            raise generics.NotFound('현재 구독 중인 구독권이 없습니다.')
    


       