from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns=[path('products/',views.ProductListCreateAPIView.as_view()),
path('products/<int:pk>/',views.ProductDetailAPIView.as_view()),
path('user-orders/',views.UserOrderAPIListView.as_view(),name='user_orders'),
path('users/',views.UserListView.as_view(),name='users')
]

router = DefaultRouter()
router.register('orders',views.OrderViewSet)
urlpatterns += router.urls