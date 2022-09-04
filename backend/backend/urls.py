"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from library.views import *  # AuthorModelViewSet, author_get, author_post, BookModelViewSet, book_get
# authtoken
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),

    path('author_get', author_get),
    path('author_get/<int:pk>', author_get),

    path('book_get', book_get),

    path('author_post', author_post),
    path('author_post/<int:pk>', author_post),
    # ApiView
    path('book_api_get_class', BookApiView.as_view()),
    path('book_api_get', book_api_get),
    # ListAPIView
    path('book_api_get_list', BookListAPIView.as_view()),
    # BookModelLimitedViewSet # вручную
    path('book_api_view_set', BookModelLimitedViewSet.as_view({'get': 'list'})),
    path('book_api_view_set/<int:pk>', BookModelLimitedViewSet.as_view({'get': 'retrieve'})),
    # action
    path('authors_api_view_set/kwargs/<str:first_name>', AuthorModelViewSet.as_view({'get': 'list'})),

    # форма authentication
    path('api-auth/', include('rest_framework.urls')),

    # authtoken
    path('api-auth-token/', views.obtain_auth_token),


]
