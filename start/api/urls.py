from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns=[path('products/',views.ProductListAPIView.as_view()),path('products/<int:pk>/',views.ProductDetailAPIView.as_view())
]

router = DefaultRouter()
router.register('orders',views.OrderViewSet)
urlpatterns += router.urls