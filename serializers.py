from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Book


class BookSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Book
        fields = '__all__'

        extra_kwargs = {
            'id':  {
                'read_only': True,
            },
        }

#



