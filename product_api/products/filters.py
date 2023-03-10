from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='iexact')
    name_contains = filters.CharFilter(field_name="name", lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = filters.CharFilter(field_name="category", lookup_expr='iexact')
    category_contains = filters.CharFilter(field_name="category", lookup_expr='icontains')
    brand = filters.CharFilter(field_name="brand", lookup_expr='iexact')
    brand_contains = filters.CharFilter(field_name="brand", lookup_expr='icontains')
    min_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='gte')
    max_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='lte')
    min_rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')
    released_after = filters.NumberFilter(field_name="created_at", lookup_expr='year__gte', help_text="year")

    class Meta:
        model = Product
        fields = ['name', 'name_contains',
                  'min_price', 'max_price',
                  'min_quantity', 'max_quantity',
                  'brand', 'brand_contains',
                  'category', 'category_contains',
                  'released_after']
