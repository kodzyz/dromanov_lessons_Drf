from django.test import TestCase
# создаем автора
from rest_framework.test import APIRequestFactory, force_authenticate
from .views import AuthorModelViewSet
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author


class AuthorTestCase(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        user = User.objects.create_superuser(username='root', password='1234')
        author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        force_authenticate(request, user=user)
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print(response.data)  # [OrderedDict([('id', 1), ('first_name', 'Александр'), ('last_name', 'Пушкин'), ('birthday_year', 1799)])]
