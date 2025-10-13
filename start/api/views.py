from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer
from api.models import Product,Order,OrderItem

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework import viewsets
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
    orders=Order.objects.prefetch_related('items').all()#Changed to optimise the querry.
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def order_details(request,pk):
    order=get_object_or_404(Order,pk=pk)
    serializer=OrderSerializer(order)
    return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    @action(detail=False,methods=['get'],url_path='user-orders')
    def user_orders(self,request):
        orders=self.get_queryset().filter(user=request.user)
        serializer=self.get_serializer(orders,many=True)
        return Response(serializer.data)