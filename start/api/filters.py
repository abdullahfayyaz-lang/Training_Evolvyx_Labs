import django_filters
from api.models import Product, Order
from rest_framework import filters

class IsStockFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        return queryset.filter(stock__gt=0)


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model =Product
        fields={
        'name':['iexact','icontains'],
        'price':['exact','lt','gt','range']

        }

class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name='created_at__date')
    class Meta:
        model = Order
        fields = {
            'status': ['exact'],
            'created_at': ['lt', 'gt', 'exact']
        }
#exmaple
#http://127.0.0.1:8000/api/products/?price__gt=100
#http://127.0.0.1:8000/api/products/?price__lt=100
#http://127.0.0.1:8000/api/products/?price__range=100,300
#http://127.0.0.1:8000/api/products/?name__contains=vet
#http://127.0.0.1:8000/api/products/?name__iexact=play%20station%205
#http://127.0.0.1:8000/api/products/?name__icontains=vet