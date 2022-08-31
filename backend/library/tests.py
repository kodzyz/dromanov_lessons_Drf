from django.test import TestCase
# setUp - метод выполн перед каждым запуском теста
# tearDown - вып после теста

# эта схема не тестирует роутер
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import AuthorModelViewSet
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author


class AuthorTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='root', password='1234')
        self.author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)

    # def tearDown(self) -> None:
    #         pass

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        force_authenticate(request, user=self.user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print(
            response.data)
