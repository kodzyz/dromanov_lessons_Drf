from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer, AuthorSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


class AuthorModelViewSet(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


def author_get(request):
    author = Author.objects.get(pk=2)
    serializer = AuthorSerializer(author)  # передаем сериализатору полученного автора
    print(serializer.data)  # внутреннее представление сериализатора = словарь
    json_data = JSONRenderer().render(serializer.data)  # JSON формат
    return HttpResponse(json_data)  # http://127.0.0.1:8000/author_get


@csrf_exempt  # исключение для POST запроса иначе будет ошибка CSRF verification failed. Request aborted
def author_post(request):
    json_data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = AuthorSerializer(data=json_data)
    elif request.method == 'PUT':
        author = Author.objects.get(pk=4)
        serializer = AuthorSerializer(author, data=json_data)  # хотим модифицировать объект -> метод update(author=instance)

    if serializer.is_valid():  # валидация данных
        author = serializer.save()  # создать и сохранить объект: вернет метод create() либо update()
        # объект переводим в JSON
        serializer = AuthorSerializer(author)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)

    return HttpResponseBadRequest()  # вернем ошибку

# NotImplementedError at /author_post
# `create()` must be implemented.
# Request Method: POST
# потому что нет явной связи с моделью
# в сериализаторе
# нет методов updata(),create()