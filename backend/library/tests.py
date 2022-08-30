from django.test import TestCase
# python manage.py test
# 0:47 Run/Debug Configuation - запуск тестов через отладчик

from rest_framework.test import APIRequestFactory


class AuthorTestCase(TestCase):
    def test_get_list(self):  # список авторов
        pass
