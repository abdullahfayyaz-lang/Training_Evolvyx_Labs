from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns=[path('products/',views.ProductListCreateAPIView.as_view()),
path('products/<int:pk>/',views.ProductDetailAPIView.as_view(),name='product-detail'),
path('user-orders/',views.UserOrderAPIListView.as_view(),name='user_orders'),
path('users/',views.UserListView.as_view(),name='users'),
path('signup/', views.signup, name='signup'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
]

router = DefaultRouter()
router.register('orders',views.OrderViewSet)
urlpatterns += router.urls