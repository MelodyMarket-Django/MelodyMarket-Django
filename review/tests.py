<<<<<<< HEAD
<<<<<<< HEAD
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Song
=======
Test.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Album
>>>>>>> 5209a3d (🔧 crud 파일추가- 초안)
=======
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Song
>>>>>>> 7fbf496 (노래, 리뷰, 장르, 좋아요 모델 추가)

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
<<<<<<< HEAD
<<<<<<< HEAD
        # 테스트를 위한 사용자와 노래 생성
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_song = Song.objects.create(title='Test Song', artist='Test Artist')
        Review.objects.create(user=test_user, song=test_song, rating=5, comment='Great Song')
=======
         # 테스트를 위한 사용자와 앨범 생성
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_album = Album.objects.create(title='Test Album', artist='Test Artist')
        Review.objects.create(user=test_user, album=test_album, rating=5, comment='Great Album')
>>>>>>> 5209a3d (🔧 crud 파일추가- 초안)
=======
        # 테스트를 위한 사용자와 노래 생성
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_song = Song.objects.create(title='Test Song', artist='Test Artist')
        Review.objects.create(user=test_user, song=test_song, rating=5, comment='Great Song')
>>>>>>> 7fbf496 (노래, 리뷰, 장르, 좋아요 모델 추가)

    def test_review_content(self):
        review = Review.objects.get(id=1)
        expected_user = f'{review.user.username}'
<<<<<<< HEAD
<<<<<<< HEAD
        expected_song = f'{review.song.title}'
        expected_rating = review.rating
        expected_comment = review.comment
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_song, 'Test Song')
        self.assertEqual(expected_rating, 5)
        self.assertEqual(expected_comment, 'Great Song')


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Song

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 테스트를 위한 사용자와 노래 생성
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_song = Song.objects.create(title='Test Song', artist='Test Artist')
        Review.objects.create(user=test_user, song=test_song, rating=5, comment='Great Song')

    def test_review_content(self):
        review = Review.objects.get(id=1)
        expected_user = f'{review.user.username}'
        expected_song = f'{review.song.title}'
        expected_rating = review.rating
        expected_comment = review.comment
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_song, 'Test Song')
        self.assertEqual(expected_rating, 5)
        self.assertEqual(expected_comment, 'Great Song')
=======
        expected_album = f'{review.album.title}'
=======
        expected_song = f'{review.song.title}'
>>>>>>> 7fbf496 (노래, 리뷰, 장르, 좋아요 모델 추가)
        expected_rating = review.rating
        expected_comment = review.comment
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_song, 'Test Song')
        self.assertEqual(expected_rating, 5)
        self.assertEqual(expected_comment, 'Great Song')


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Song

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 테스트를 위한 사용자와 노래 생성
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_song = Song.objects.create(title='Test Song', artist='Test Artist')
        Review.objects.create(user=test_user, song=test_song, rating=5, comment='Great Song')

<<<<<<< HEAD
    def test_create_review(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('review-create', kwargs={'album_id': self.album.id})
        data = {'rating': 5, 'comment': 'Great album!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
>>>>>>> 5209a3d (🔧 crud 파일추가- 초안)
=======
    def test_review_content(self):
        review = Review.objects.get(id=1)
        expected_user = f'{review.user.username}'
        expected_song = f'{review.song.title}'
        expected_rating = review.rating
        expected_comment = review.comment
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_song, 'Test Song')
        self.assertEqual(expected_rating, 5)
        self.assertEqual(expected_comment, 'Great Song')
>>>>>>> 7fbf496 (노래, 리뷰, 장르, 좋아요 모델 추가)

