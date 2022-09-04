from rest_framework.routers import DefaultRouter
from .views import AuthorModelViewSet, BookModelViewSet
from django.urls import path, include

app_name = 'library'

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)

urlpatterns = [
    path('', include(router.urls))

]
