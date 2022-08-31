from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from .views import AuthorModelViewSet
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author

# POST-запрос создания модели

class AuthorClientTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='root', password='1234')
        self.author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)

    def test_post(self):
        self.client.login(username='root', password='1234')
        #self.client.force_login(user=self.user)
        response = self.client.post('/api/authors/', {
            "first_name": "Александр",
            "last_name": "Грин",
            "birthday_year": 1860
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(pk=response.data.get('id'))
        self.assertEqual(author.last_name, 'Грин')



