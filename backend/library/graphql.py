import graphene
from graphene_django import DjangoObjectType
from .models import Author, Book


class AuthorObjectType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class BookObjectType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorObjectType)

    def resolve_all_authors(self, info):
        return Author.objects.all()

    all_books = graphene.List(BookObjectType)

    def resolve_all_books(self, info):
        # return Book.objects.all()
        return Author.objects.get(pk=1).book_set.all()

    # {
    #   allBooks{title}
    # }

    # получение автора по id
    get_author_by_id = graphene.Field(AuthorObjectType, pk=graphene.Int(required=True))

    def resolve_get_author_by_id(self, info, pk):  # получает id
        return Author.objects.get(pk=pk)

    # получение более одной модели


schema = graphene.Schema(query=Query)

