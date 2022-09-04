from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Author, Book


class AuthorSerializer(Serializer):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    birthday_year = IntegerField()

    def update(self, instance, validated_data):  # PUT запрос: редактирование модели
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)  # значение по умолчанию для метода PATCH
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        instance.save()
        return instance

    def create(self, validated_data):  # создает объкт из валидированных данных
        author = Author(**validated_data)
        author.save()
        return author

    def validate_birthday_year(self,
                               value):  # валидация по полю: PATCH "birthday_year": 2010 -> {"birthday_year":["18+"]}
        if value > 2004:
            raise ValidationError('18+')
        return value

    def validate(self, attrs):  # валидация по более чем одному полю
        if attrs.get('last_name') == 'Бредбери' and attrs.get('birthday_year') != 1920:
            raise ValidationError(
                'birthday_year must be 1920')  # POST {"non_field_errors":["birthday_year must be 1920"]}
        return attrs


class BookSerializer(Serializer):
    title = CharField(max_length=64)
    authors = AuthorSerializer(many=True) # много авторов для одной книжки


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        # fields = ['first_name', 'last_name']
        fields = '__all__'

class AuthorModelSerializerV2(ModelSerializer):  # API version 2
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']


class BookModelSerializer(ModelSerializer):
    #authors = StringRelatedField(many=True)  # из модели берется def __str__(self):
    class Meta:
        model = Book
        fields = '__all__'
