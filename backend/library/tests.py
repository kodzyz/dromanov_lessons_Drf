from django.test import TestCase
#
from rest_framework.test import APIRequestFactory  # класс для генерации запросов
from .views import AuthorModelViewSet
from rest_framework import status


class AuthorTestCase(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        # AssertionError: 401 != 200 потому что не залогинились -> permissions.IsAuthenticated
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # не залогинились = 401
