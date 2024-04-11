from django.urls import reverse_lazy
<<<<<<< HEAD
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from .models import Song, Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    리뷰 데이터에 대한 CRUD를 담당.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        리뷰 생성 시, 현재 로그인한 사용자를 리뷰 작성자로 자동 설정.
        """
        serializer.save(user=self.request.user)

class ReviewListView(LoginRequiredMixin, ListView):
    """
    리뷰 목록을 보여주는 뷰.
    """
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

class ReviewDetailView(LoginRequiredMixin, DetailView):
    """
    리뷰 상세 정보를 보여주는 뷰.
    """
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    새로운 리뷰를 생성하는 뷰.
    """
    model = Review
    template_name = 'reviews/review_form.html'
    fields = ['song', 'rating', 'comment']

    
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    기존 리뷰를 수정하는 뷰.
    """
    model = Review
    template_name = 'reviews/review_form.html'
    fields = ['song', 'rating', 'comment']

   

    def test_func(self):
        """
        사용자가 자신의 리뷰만 수정할 수 있도록 테스트.
        """
        review = self.get_object()
        return self.request.user == review.user

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    리뷰를 삭제하는 뷰.
    """
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review-list')

    def test_func(self):
        """
        사용자가 자신의 리뷰만 삭제할 수 있도록 테스트.
        """
        review = self.get_object()
        return self.request.user == review.user

class SignUpView(CreateView):
    """
    사용자 등록을 위한 뷰.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
=======
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import Album, Review
from .serializers import AlbumSerializer, ReviewSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """앨범 데이터에 대한 CRUD 및 추가 정보 제공을 담당하는"""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """특정 앨범에 대한 모든 리뷰를 반환합니다."""
        album = self.get_object()
        reviews = self.get_reviews(album)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        """특정 앨범의 평균 평점을 반환합니다."""
        album = self.get_object()
        average_rating = self.get_average_rating(album)
        return Response({'average_rating': average_rating})

def get_average_rating(self, album):
        """앨범의 평균 평점을 계산하는 메소드."""
        average = album.reviews_set.aggregate(Avg('rating'))['rating__avg’]
        return round(average, 2) if average else 0

class ReviewViewSet(viewsets.ModelViewSet):
    """리뷰 데이터에 대한 CRUD를 담당하는 ViewSet."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """리뷰 생성 시, 현재 로그인한 사용자를 리뷰 작성자로 자동 설정."""
        serializer.save(user=self.request.user)




class ReviewListView(ListView):
model = Review
template_name = 'reviews/review_list.html'
context_object_name = 'reviews'
paginate_by = 10  


class ReviewDetailView(DetailView):
model = Review
template_name = 'reviews/review_detail.html'


class ReviewCreateView(LoginRequiredMixin, CreateView):
model = Review
template_name = 'reviews/review_form.html'
fields = ['title', 'content', 'rating']

```
def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

```


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
model = Review
template_name = 'reviews/review_form.html'
fields = ['title', 'content', 'rating']

```
def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def test_func(self):
    review = self.get_object()
    return self.request.user == review.user

```


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
model = Review
template_name = 'reviews/review_confirm_delete.html'
success_url = reverse_lazy('review-list')

def test_func(self):
    review = self.get_object()
    return self.request.user == review.user


class SignUpView(generic.CreateView):
    """사용자 등록을 위한 View."""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


>>>>>>> 5209a3d (🔧 crud 파일추가- 초안)
