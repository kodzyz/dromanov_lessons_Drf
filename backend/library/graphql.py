import graphene
from graphene_django import DjangoObjectType
from .models import Author


# связь с моделью = похоже на serializer
class AuthorObjectType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorObjectType)  # команда return List авторов

    def resolve_all_authors(self, info):
        return Author.objects.all()


schema = graphene.Schema(query=Query)

# {
#   allAuthors {
#     id
#     firstName
#     lastName
#     birthdayYear
#   }
# }