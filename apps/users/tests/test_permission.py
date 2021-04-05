import os
import json
from django.core.management import call_command
from django.test import TestCase
from django.urls.base import reverse
from apps.users.models import User


class BaseTest(TestCase):
    user1 = {
        'email': 'test_user@gmail.com',
        'name': 'test',
        'last_name': 'user',
        'password': 'test'
    }
    user2 = {
        'email': 'new_user@gmail.com',
        'name': 'new',
        'last_name': 'user',
        'password1': 'test',
        'password2': 'test',
    }

    def setUp(self):
        register_url = reverse('user:register')
        user1 = User.objects.create(**self.user1)
        self.client.post(register_url, self.user2, format='text/html')
        self.url1 = reverse('feed:user_feed', kwargs={'pk': user1.id})
        user2 = User.objects.filter(email=self.user2.get('email')).first()
        self.url2 = reverse('feed:user_feed', kwargs={'pk': user2.id})
        return super().setUp()


class PermissionTest(BaseTest):

    def test_users_in_db(self):
        self.assertEqual(User.objects.count(), 2)

    def test_user_without_permissions(self):
        response = self.client.get(self.url1)
        self.assertEqual(response.status_code, 403)
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, 200)
