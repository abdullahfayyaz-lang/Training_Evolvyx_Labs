from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter 

urlpatterns=[path('products/',views.product_list),path('products/<int:pk>/',views.product_details)
]

router = DefaultRouter()
router.register('orders',views.OrderViewSet)
urlpatterns += router.urls