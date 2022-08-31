import random

from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase
from .views import AuthorModelViewSet
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author
from mixer.backend.django import mixer


# генерация тестовых данных (автоматически)
# pip install mixer

class AuthorClientTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='root', password='1234')
        #self.author = mixer.blend(Author)
        # self.author = mixer.cycle(5).blend(Author) # 5 авторов
        # self.author = mixer.blend(Author, birthday_year=1799)  # одно поле генерится с конкретным заначением
        self.author = mixer.blend(Author, birthday_year=mixer.sequence(lambda c: int(random.random()*2000)))  # от 0 до 2000

    def test_post(self):
        self.client.login(username='root', password='1234')
        response = self.client.post('/api/authors/', {  # debug 
            "first_name": "Александр",
            "last_name": "Грин",
            "birthday_year": 1860
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author = Author.objects.get(pk=response.data.get('id'))
        self.assertEqual(author.last_name, 'Грин')
