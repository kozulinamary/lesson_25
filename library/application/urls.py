from django.urls import path, include
from .endpoints import AuthorListAPIView,\
    AuthorListCreateAPIView, AuthorRUDAPIView, BookAPIViewset,\
    AuthorBooksAPIView, PublishingHouseAPIViewset, PublishingHouseAuthorAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("book", BookAPIViewset)
router_2 = DefaultRouter()
router_2.register("publishing_house", PublishingHouseAPIViewset)


urlpatterns = [
    path('author_list/', AuthorListAPIView.as_view(), name='author_list'),
    path('author_create/', AuthorListCreateAPIView.as_view(), name='author_create'),
    path("author_rud/<int:pk>", AuthorRUDAPIView.as_view(), name="author_rud"),
    path("", include(router.urls), name="book_viewset"),
    path("author/<int:id>/books", AuthorBooksAPIView.as_view(), name="author_books"),
    path("", include(router_2.urls), name="publishing_house_viewset"),
    path("publishing_house/<int:id>/authors/", PublishingHouseAuthorAPIView.as_view(), name="publishing_house_authors"),

]

