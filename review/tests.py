Test.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Album

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
         # 테스트를 위한 사용자와 앨범 생성
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_album = Album.objects.create(title='Test Album', artist='Test Artist')
        Review.objects.create(user=test_user, album=test_album, rating=5, comment='Great Album')

    def test_review_content(self):
        review = Review.objects.get(id=1)
        expected_user = f'{review.user.username}'
        expected_album = f'{review.album.title}'
        expected_rating = review.rating
        expected_comment = review.comment
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_album, 'Test Album')
        self.assertEqual(expected_rating, 5)
        self.assertEqual(expected_comment, 'Great Album')




from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Album

class ReviewCreateAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # 테스트 사용자와 앨범 생성
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.album = Album.objects.create(title='Test Album', artist='Test Artist')

    def test_create_review(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('review-create', kwargs={'album_id': self.album.id})
        data = {'rating': 5, 'comment': 'Great album!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

