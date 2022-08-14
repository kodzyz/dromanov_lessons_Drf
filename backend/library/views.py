from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()
