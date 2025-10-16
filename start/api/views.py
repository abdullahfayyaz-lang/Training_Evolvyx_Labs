from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from api.serializers import ProductSerializer,OrderItemSerializer,OrderSerializer,OrderCreateSerializer, UserSeralizer
from api.models import Product,Order,OrderItem, User
from rest_framework import generics , filters
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,action,permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from api.filters import ProductFilter, IsStockFilterBackend, OrderFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.throttling import ScopedRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken# for jwt one
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import User
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# class ProductListAPIView(generics.ListAPIView):
#     queryset=Product.objects.all()# now it will only return the products with stock greater then 0
#     serializer_class=ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    throttle_scope = 'products'
    throttle_classes=[ScopedRateThrottle]
    queryset=Product.objects.order_by('pk')
    serializer_class=ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, IsStockFilterBackend]  
    filterset_class = ProductFilter
    search_fields = ['=name', 'description'] #put (=) infront of field if you want exact match
    ordering_fields=['name','price','stock']
    pagination_class=LimitOffsetPagination
    # pagination_class.page_size=2
    # pagination_class.page_query_param='pagenum'
    # pagination_class.page_size_query_param='size'
    # pagination_class.max_page_size=6

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
@login_required(login_url='login')#this will check if user is loged in or not if user is loged in it will allow it to use this view else it will redirect user to login page and make sure user to login
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
    throttle_scope = 'orders'
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    filterset_class = OrderFilter
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        # can also check if POST: if self.request.method == 'POST'
        if self.action == 'create' or self.action =='update' :
            return OrderCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)


class UserListView(generics.ListAPIView):
    queryset=User.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=UserSeralizer
    pagination_class=None

# Signup View-> Using simple django authntication
# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Account created successfully!")
#             return redirect('login')
#         else:
#             messages.error(request, "Please correct the error below.")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'signup.html', {'form': form})
# Signup View-> Using Jwt  authntication

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            # Generate JWT tokens (optional for API use)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            # Store tokens in session if needed (optional)
            request.session['access_token'] = access_token
            request.session['refresh_token'] = str(refresh)

            messages.success(request, "✅ Account created successfully! You can now log in.")
            return redirect('login')  # Use named route instead of hardcoding URL
        else:
            messages.error(request, "Please correct the errors below and try again.")
    else:
        form = CustomUserCreationForm()
    for msg in messages.get_messages(request):
        print(f"[{msg.level_tag.upper()}] {msg.message}")
    return render(request, 'signup.html', {'form': form})
# Login View-> Using simple django authntication
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             return redirect('http://127.0.0.1:8000/api/orders/')  # Redirect to the API orders endpoint
#         else:
#             messages.error(request, "Invalid credentials.")
#     return render(request, 'login.html')


#login implementation using JWT token
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authenticate the user
            login(request, user)
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            # Return the JWT token in the response or redirect to the desired API
            response_data = {
                'access_token': access_token,
                'refresh_token': str(refresh),
            }
            # Redirect to the orders API with the JWT token
            return redirect(f'http://127.0.0.1:8000/api/orders/')

        else:
            messages.error(request, "Invalid credentials.")
    
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')