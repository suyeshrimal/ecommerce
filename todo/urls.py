from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter
routers=SimpleRouter()

routers.register('categories',CategoryViewset,basename='categories')
routers.register('product',ProductViewset,basename='product')

urlpatterns = [
    # path("categories",CategoryList.as_view()),
    # path("categories/<pk>",CategoryDetail.as_view()),
    # path("product",ProductList.as_view()),
    # path("product/<pk>/",ProductDetail.as_view()),
]+routers.urls
