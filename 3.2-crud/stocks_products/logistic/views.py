from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['title', 'description']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products']
    search_field = ['products']
    # при необходимости добавьте параметры фильтрации
