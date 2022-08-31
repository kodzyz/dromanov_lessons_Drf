from django.test import TestCase
# включает в себя механизм создания клиента client = APIClient()
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from .views import AuthorModelViewSet
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author


class AuthorTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='root', password='1234')
        self.author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        force_authenticate(request, user=self.user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class AuthorClientTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='root', password='1234')
        self.author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)

    def test_get_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
