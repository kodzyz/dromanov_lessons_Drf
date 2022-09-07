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
        return Book.objects.all()

    # получение автора по id
    get_author_by_id = graphene.Field(AuthorObjectType, pk=graphene.Int(required=True))

    # Field-сложное поле AuthorObjectType-тип возвращаемых данных
    # ..., pk=-значение которое нужно получить

    def resolve_get_author_by_id(self, info, pk):  # получает id
        return Author.objects.get(pk=pk)


schema = graphene.Schema(query=Query)

# {
#   getAuthorById(pk:1){
#     id
#     firstName
#     lastName
#     birthdayYear
#   }
# }