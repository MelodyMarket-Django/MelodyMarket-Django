from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        print('-- main app test START --')
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='jsyoo',
            password='iloveit1229!'
        )
        self.user.save()

        self.subscription = Subscription.objects.create(
            user = 'self.user',
            type = '1개월권',
            start_date = '2024-04-11 15:30:00',
            end_date = '2024-05-11 15:30:00',
            price = '100',
            active = True,
        )

        self.subscription.save()

        print("-- main app test END --")

    def subscription_read(self):
        print("-- subscription_read test START --")
        print("-- 비회원 읽기 테스트 --")
        response = self.client.get('/subscription/detail/')
        self.assertEqual(response.status_code, 403)

        print("-- 회원 읽기 테스트 --")
        self.client.login(username = 'jsyoo', password = 'iloveit1229!')
        response = self.client.get('/subscription/detail/')
        self.assertEqual(response.status_code, 200)
        
        print('-- subscription_read test END--')


    def subscription_create(self):
        print("-- subscription_create test START --")

        print("-- 비회원 작성 테스트 --")
        response = self.client.post(
            '/buy/voucher/',
            {
            'user': 'self.user',
            'type': '1개월권',
            'start_date': '2024-04-11 15:30:00',
            'end_date': '2024-05-11 15:30:00',
            'price': '100',
            'active': True,
            },
            format = 'json',
        )
        self.assertEqual(response.status_code, 403)


        print("-- 회원 작성 테스트 --")
        response = self.client.post(
            '/buy/voucher/',
            {
            'user': 'self.user',
            'type': '1개월권',
            'start_date': '2024-04-11 15:30:00',
            'end_date': '2024-05-11 15:30:00',
            'price': '100',
            'active': True,
            },
            format = 'json',
        )
        self.assertEqual(response.status_code, 201)

        print("-- subscription_create test END --")

    def subscription_update(self):
        print("-- subscription_update test START --")
        self.client.login(username='jsyoo', password='iloveit1229!')
        response = self.client.put(
            f'/subscription/{self.subscription.id}/',
            {
                'type': '3개월권',
                'start_date': '2024-04-11 15:30:00',
                'end_date': '2024-07-11 15:30:00',
                'price': '300',
                'active': True,
            },
            format='json',
        )
        self.assertEqual(response.status_code, 200)
        print("-- subscription_update test END --")

    def subscription_delete(self):
        print("-- subscription_delete test START --")
        self.client.login(username='jsyoo', password='iloveit1229!')
        response = self.client.delete(f'/subscription/{self.subscription.id}/')
        self.assertEqual(response.status_code, 204)
        print("-- subscription_delete test END --")

