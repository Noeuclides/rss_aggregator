import os
import json
from django.core.management import call_command
from django.test import TestCase
from django.urls.base import reverse
from apps.users.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('user:register')
        self.login_url = reverse('user:login')
        self.user = {
            'email': 'test_user@gmail.com',
            'name': 'test',
            'last_name': 'user',
            'password1': 'test',
            'password2': 'test',
        }
        return super().setUp()


class RegisterTest(BaseTest):

    def test_can_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_can_register(self):
        response = self.client.post(
            self.register_url, self.user, format='text/html')
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.filter(email=self.user.get('email')).first()
        self.assertRedirects(
            response, reverse(
                'feed:user_feed', kwargs={
                    'pk': user.id}))


class LoginTest(BaseTest):

    def test_can_view_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_can_login(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.filter(email=self.user.get('email')).first()
        response = self.client.post(
            self.login_url, self.user, format='text/html')
        self.assertRedirects(
            response, reverse(
                'feed:user_feed', kwargs={
                    'pk': user.id}))
