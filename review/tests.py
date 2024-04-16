from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review, Song

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 사용자와 노래 객체를 테스트 목적으로 생성합니다.
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_song = Song.objects.create(title='Test Song', artist='Test Artist')
        Review.objects.create(user=test_user, song=test_song, rating=5, comment='Great Song')

    def test_review_content(self):
        # 리뷰 객체의 내용을 검사합니다.
        review = Review.objects.get(id=1)
        expected_user = f'{review.user.username}'
        expected_song = f'{review.song.title}'
        expected_rating = review.rating
        expected_comment = review.comment
        self.assertEqual(expected_user, 'testuser')
        self.assertEqual(expected_song, 'Test Song')
        self.assertEqual(expected_rating, 5)
        self.assertEqual(expected_comment, 'Great Song')

    def test_create_review(self):
        # 사용자 로그인을 시도합니다.
        self.client.login(username='testuser', password='12345')
   
        # 리뷰 생성 API를 호출합니다.
        url = reverse('review-create', kwargs={'song_id': self.test_song.id})
        data = {'rating': 5, 'comment': 'Great song!'}
        response = self.client.post(url, data, format='json')
        # 생성된 리뷰의 HTTP 상태 코드를 검증합니다.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
