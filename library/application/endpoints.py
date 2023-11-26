from rest_framework.generics import ListAPIView,\
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import AuthorSerializer, BookSerializer, PublishingHouseSerializer
from .models import Author, Book, PublishingHouse
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.AllowAny]


class AuthorListCreateAPIView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAdminUser]

class AuthorRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAdminUser]


class BookAPIViewset(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]
class AuthorBooksAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        author = self.kwargs["id"]
        return Book.objects.filter(author_id=author)

class PublishingHouseAPIViewset(ModelViewSet):
    serializer_class = PublishingHouseSerializer
    queryset = PublishingHouse.objects.all()
    permission_classes = [permissions.IsAdminUser]

class PublishingHouseAuthorAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        publishing_house = self.kwargs["id"]
        return Author.objects.filter(publiszing_id=publishing_house)








