from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Author


class AuthorSerializer(Serializer):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    birthday_year = IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):  # создает объкт из валидированных данных
        author = Author(**validated_data)
        author.save()
        return author


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        # fields = ['first_name', 'last_name']
        fields = '__all__'
