from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from .views import AuthorModelViewSet
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author


class AuthorClientTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='root', password='1234')
        self.author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)

    def test_get_list(self):
        self.client.login(username='root', password='1234')  # знаем логин и пароль
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.client.logout()
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

