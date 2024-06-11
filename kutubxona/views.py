from rest_framework import viewsets, filters
from .models import Book, Review, User
from .serializers import BookSerializer, ReviewSerializer, UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    reviews = ReviewSerializer(many=True, read_only=True)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author')

