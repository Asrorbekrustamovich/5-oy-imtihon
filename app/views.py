from django.shortcuts import render
from rest_framework.views import Response
from .serializers import *
from  rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class Product_imageCreateLIst(generics.ListCreateAPIView):
    queryset = Product_Images.objects.all()
    serializer_class = Prodcut_imagesSerializer
class Product_imageUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_Images.objects.all()
    serializer_class = Prodcut_imagesSerializer
class CategoryCreateList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class SellerCreateList(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
class SellerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
class ProductsCreateList(generics.ListCreateAPIView):
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('Category', 'name')
    search_fields = ['name']
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
class ProductsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
class Get_selled_proudcts_count_and_all_products_count_and_benefit_for_one_seller(generics.ListAPIView):
    serializer_class = ProductsSerializer
    def get_queryset(self):
        seller_id = self.kwargs['seller_id']
        seller=Seller.objects.get(id=seller_id)
        products = Products.objects.filter(seller=seller)
        
        sell_count = sum(product.betlar_soni for product in products)
        all_count = products.count()
        benefit = sum(product.price * product.betlar_soni for product in products)
        
        data = {
            'sell_count': sell_count,
            'all_count': all_count,
            'benefit': benefit,
            'products': ProductsSerializer(products, many=True).data
        }
        
        return Response(data)
