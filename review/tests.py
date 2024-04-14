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

