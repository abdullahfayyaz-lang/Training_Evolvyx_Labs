from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer
from api.models import Product,Order,OrderItem
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,action,permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from api.filters import ProductFilter
# Create your views here.

# class ProductListAPIView(generics.ListAPIView):
#     queryset=Product.objects.all()# now it will only return the products with stock greater then 0
#     serializer_class=ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filterset_class=ProductFilter

    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method =='POST':#checks if request method is post only admin can aceess it
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookip_url_kwarg="product_id"##to chnage url parameter else then pk we use this 
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['PUT','PATCH',"DELETE"]:#checks if request method id put,patch or delete then only admin can aceess it
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()


# @api_view(['GET'])
# def product_list(request):
#     products=Product.objects.all()
#     serializer=ProductSerializer(products,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def product_details(request,pk):
#     products=get_object_or_404(Product,pk=pk)
#     serializer=ProductSerializer(products)
#     return Response(serializer.data)


# RetrieveUpdateDestroyAPIView
# Used for read-write-delete endpoints to represent a single model instance.

# Provides get, put, patch and delete method handlers.

# Extends: GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

@api_view(['GET'])
def order_list(request):
    orders=Order.objects.prefetch_related('items').all()#Changed to optimise the querry.
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_details(request,pk):
    order=get_object_or_404(Order,pk=pk)
    serializer=OrderSerializer(order)
    return Response(serializer.data)
class UserOrderAPIListView(generics.ListAPIView):
    queryset=Order.objects.prefetch_related('items').all()
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(user=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    @action(detail=False,methods=['get'],url_path='user-orders')
    def user_orders(self,request):
        orders=self.get_queryset().filter(user=request.user)
        serializer=self.get_serializer(orders,many=True)
        return Response(serializer.data)