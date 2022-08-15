from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Author, Book
from .serializers import AuthorModelSerializer, AuthorSerializer, BookModelSerializer, BookSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
import io
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, \
    get_object_or_404  # конкретизированные views


class AuthorModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]  # явно определяем список renderer_classes
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()

    @action(detail=True, methods=['get'])  # команда получения имени автора
    def get_author_mane(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return Response({'name': str(author)})  #/api/authors/1/get_author_mane/

    def get_queryset(self):
        return Author.objects.filter(first_name=self.kwargs['first_name'])


class BookModelViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


class BookModelLimitedViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):  # не позволяет создавать(mixins.CreateModelMixin) и удалять(mixins.DestroyModelMixin): собираем из нужных операций
    """
        `retrieve()`, `update()`, `partial_update()`, and `list()` actions.
    """
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


class BookApiView(APIView):
    renderer_classes = [JSONRenderer]  # можем задавать способ render

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)  # разница не задаем render


class BookListAPIView(ListAPIView):  # глагол GET
    renderer_classes = [JSONRenderer]
    serializer_class = BookSerializer
    queryset = books = Book.objects.all()


@api_view(['GET'])  # аналогично APIView
@renderer_classes([JSONRenderer])
def book_api_get(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


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
