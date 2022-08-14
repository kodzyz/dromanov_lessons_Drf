from rest_framework.serializers import ModelSerializer
from .models import Author


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        # fields = ['first_name', 'last_name']
        fields = '__all__'