from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book
from .serializers import AuthorModelSerializer, AuthorSerializer, BookModelSerializer, BookSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
import io


class AuthorModelViewSet(ModelViewSet):
    #renderer_classes = [JSONRenderer, BrowsableAPIRenderer]  # явно определяем список renderer_classes
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()


class BookModelViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


def book_get(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


def author_get(request, pk=None):
    if pk is not None:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)  # передаем сериализатору полученного автора
    else:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)  # many=True передаем не один объект

    json_data = JSONRenderer().render(serializer.data)  # JSON формат
    return HttpResponse(json_data)  # http://127.0.0.1:8000/author_get


@csrf_exempt  # исключение для POST запроса иначе будет ошибка CSRF verification failed. Request aborted
def author_post(request, pk=None):
    json_data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':  # маршрутизация на метод create
        serializer = AuthorSerializer(data=json_data)
    elif request.method == 'PUT':  # маршрутизация на метод update
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author,
                                      data=json_data)  # хотим модифицировать объект -> метод update(author=instance)
    elif request.method == 'PATCH':
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, data=json_data,
                                      partial=True)  # partial=True частично переданный набор данных считается валидным

    if serializer.is_valid():  # валидация данных
        author = serializer.save()  # создать и сохранить объект: вернет метод create() либо update()

        # объект переводим в JSON
        serializer = AuthorSerializer(author)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)

    return HttpResponseBadRequest(JSONRenderer().render(serializer.errors))  # вернем на frontend ошибку валидации
