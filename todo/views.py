from django.http import Http404
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .pagination import CustomPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import *
from django_filters import rest_framework as filters
from rest_framework import filters as f
from .filters import ProductFilter
from django.db.models import Count

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(
        IsAuthenticatedOrReadOnly,
        IsAdminOrNot,
    )
    def get_queryset(self):
        return Category.objects.prefetch_related('products') \
        .annotate(
            total_product=Count("products")
        ) \
        .all()

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.select_related('category').all()
    serializer_class=ProductSerializer
    pagination_class=CustomPagination
    filter_backends=(filters.DjangoFilterBackend,f.SearchFilter,)
    filterset_class=ProductFilter
    search_fields=('name',)

class Customer(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer()



# class CategoryList(generics.ListCreateAPIView,generics.GenericAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer


# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#      queryset=Category.objects.all()
#      serializer_class=CategorySerializer

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Category.objects.all()
#     serializer_class=CategorySerializer
        
        
# # @api_view(['GET','DELETE','PUT'])
# # def category_detail(request,pk):
    
# #     category=get_object_or_404(Category,pk=pk)
# #     if request.method=="GET":
# #         serializer=CategorySerializer(category)
# #         return Response(
# #             serializer.data,
# #         )
# #     if request.method=="DELETE":
# #         category.delete()
# #         return Response(
# #             status=status.HTTP_204_NO_CONTENT
# #         )
# #     if request.method=="PUT":
        
# #         serializer=CategorySerializer(category,data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(
# #             {
# #                 'details':'The data has been successfully updated as you wish !!'
# #             }
            
# #         )
    
    
    
    
    
# class ProductList(APIView):
    
#     def get(self,request):
#         product=Product.objects.all()
#         serializer=ProductSerializer(product,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# class ProductDetail(APIView):
    
#     def get_object(self,pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response({
#                 'details':'get object !!'
#             })  
            
#     def get(self,request,pk):
#         product=self.get_object(pk)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         product=self.get_object(pk)
#         serializer=ProductSerializer(product,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({
#             'details' : 'The value has been successfully updated !!'
#         })
    
#     def delete(self,request,pk):
#         product=self.get_object(pk)
#         product.delete()
#         return Response({
#             'details':'Successfully deleted !!'
#         })
    
          


