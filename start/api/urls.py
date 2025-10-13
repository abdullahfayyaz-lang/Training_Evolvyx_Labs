from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns=[path('products/',views.ProductListAPIView.as_view()),path('products/<int:pk>/',views.ProductDetailAPIView.as_view()),path('user-orders/',views.UserOrderAPIListView.as_view())
]

