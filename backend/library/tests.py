from django.test import TestCase
# конструируем request для наших запросов
# передаём запрос в view
# после передачи запроса получаем ответ response и проверяем статус
from rest_framework.test import APIRequestFactory  # класс для генерации запросов
from .views import AuthorModelViewSet
from rest_framework import status


class AuthorTestCase(TestCase):
    def test_get_list(self):  # список авторов
        factory = APIRequestFactory()
        request = factory.get('api/authors/')  # конструируем GET запрос по URL
        view = AuthorModelViewSet.as_view({'get': 'list'})  # связать запрос get с методом list
        response = view(request)  # запускаем views от запроса
        # проверка через предположение что статус = 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # AssertionError: 401 != 200 -> IsAuthenticated
