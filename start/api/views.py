from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer
from api.models import Product,Order,OrderItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def product_list(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_details(request,pk):
    products=get_object_or_404(Product,pk=pk)
    serializer=ProductSerializer(products)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders=Order.objects.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_details(request,pk):
    order=get_object_or_404(Order,pk=pk)
    serializer=OrderSerializer(order)
    return Response(serializer.data)