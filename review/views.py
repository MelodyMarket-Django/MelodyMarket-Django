from django.urls import reverse_lazy

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

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
(노래, 리뷰, 장르, 좋아요 모델 추가)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from .models import Song, Review, Genre
from .serializers import ReviewSerializer, SongSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    리뷰 데이터에 대한 CRUD
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewListView(LoginRequiredMixin, ListView):
    """
    리뷰 목록을 보여주는 
    """
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

class ReviewDetailView(LoginRequiredMixin, DetailView):
    """
    리뷰 상세 정보를 보여주는
    """
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    새로운 리뷰를 생성하는 
    """
    model = Review
    template_name = 'reviews/review_form.html'
    fields = ['song', 'rating', 'comment']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    기존 리뷰를 수정하는
    """
    model = Review
    template_name = 'reviews/review_form.html'
    fields = ['song', 'rating', 'comment']

    def test_func(self):
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
        review = self.get_object()
        return self.request.user == review.user

# Song 
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'artist', 'genres__name']

class SignUpView(CreateView):
    """
    사용자 등록
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# 시리얼라이저 
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'genres', 'cover_image', 'release_date', 'created_by']

(🔧 crud 파일추가- 초안)
