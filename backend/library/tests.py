from django.test import TestCase
# создаем пользователя
# логинимся: аутентификация
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import AuthorModelViewSet
from rest_framework import status
from django.contrib.auth.models import User


class AuthorTestCase(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        user = User.objects.create_superuser(username='root', password='1234')
        force_authenticate(request, user=user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

