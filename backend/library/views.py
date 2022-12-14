from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Author, Book
from .serializers import AuthorModelSerializer, AuthorSerializer, BookModelSerializer, BookSerializer, \
    AuthorModelSerializerV2
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
import io
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, \
    get_object_or_404  # конкретизированные views
from rest_framework.pagination import LimitOffsetPagination
# authorization
from rest_framework.permissions import IsAuthenticated, AllowAny, \
    IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission,\
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class CustomPermissions(BasePermission):  # собственные права

# 'Ctrl + o' - выводит все методы
    def has_permission(self, request, view):  # переопределим метод
        return request.user and request.user.username == 'root'


class AuthorLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2  # сколько записей по умолчанию будет выводиться

# делаем точку разделения API version
# делаем динамический serializer
class AuthorModelViewSet(ModelViewSet):
    # pagination_class = AuthorLimitOffsetPagination
    #permission_classes = [DjangoModelPermissions]  # система прав Django на модели через /admin (user:test pass:tNbby!5X!624L2c)
    #serializer_class = AuthorModelSerializer # статический serializer не указываем, а реализовываем метод get_serializer_class
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':  # как передать version в request?
            return AuthorModelSerializerV2
        return AuthorModelSerializer  # version by default

    @action(detail=True, methods=['get'])  # команда получения имени автора
    def get_author_mane(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return Response({'name': str(author)})  # /api/authors/1/get_author_mane/

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name', None)  # если есть переданный аргумент
        if first_name:
            return Author.objects.filter(
                first_name=first_name)  # http://127.0.0.1:8000/api/authors/?first_name=Александр
        return Author.objects.all()


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
