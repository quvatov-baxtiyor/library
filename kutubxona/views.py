from rest_framework import viewsets, filters
from .models import Book, Review, User
from .serializers import BookSerializer, ReviewSerializer, UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    reviews = ReviewSerializer(many=True, read_only=True)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author')


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


