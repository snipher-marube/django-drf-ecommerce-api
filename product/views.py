from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product, Brand, Category
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer

class CategoryViewSet(viewsets.Vieset):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class BrandViewSet(viewsets.Vieset):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.Vieset):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
