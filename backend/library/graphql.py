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


schema = graphene.Schema(query=Query)

# {
#    allBooks {
#     id
#     title
#     authors{
#       id
#       firstName
#       lastName
#       birthdayYear
#     }
#   }
# }

# {
#   allBooks{
#     id
#     title
#     authors{
#       id
#     }
#   }
#   allAuthors{
#     id
#     firstName
#     lastName
#     birthdayYear
#   }
# }
