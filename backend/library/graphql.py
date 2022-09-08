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

    # получение автора по id
    get_author_by_id = graphene.Field(AuthorObjectType, pk=graphene.Int(required=True))

    def resolve_get_author_by_id(self, info, pk):  # получает id
        return Author.objects.get(pk=pk)

    # получение автора по имени
    get_author_by_name = graphene.List(AuthorObjectType,
                                       first_name=graphene.String(required=False),
                                       last_name=graphene.String(required=False)
                                       )

    def resolve_get_author_by_name(self, info, first_name=None, last_name=None):
        if not first_name and not last_name:
            return Author.objects.all()
        params = {}
        if first_name:
            params['first_name__contains'] = first_name  # params['first_name'] полное/частичное совпадение
        if last_name:
            params['last_name__contains'] = last_name  # params['last_name']
        return Author.objects.filter(**params)


# создание автора
class AuthorCreateMutation(graphene.Mutation):
    # список входных параметров
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorObjectType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday_year):
        author = Author(first_name=first_name, last_name=last_name, birthday_year=birthday_year)
        author.save()
        return cls(author)


# применение mutate: команды которые реализцую мутацию
class Mutations(graphene.ObjectType):
    create_author = AuthorCreateMutation.Field()


# регистрация mutate
schema = graphene.Schema(query=Query, mutation=Mutations)
