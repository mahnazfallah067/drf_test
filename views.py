
from rest_framework.generics import ListAPIView
from project.models import Book
from project.serializers import BookSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



