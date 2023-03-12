from django_filters import rest_framework as filters
from .models import Product, CartItem, Cart, Category


class ProductFilter(filters.FilterSet):
    category__name = filters.CharFilter(lookup_expr='iexact')
    name = filters.CharFilter(field_name="name", lookup_expr='iexact')
    name_contains = filters.CharFilter(field_name="name", lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    brand = filters.CharFilter(field_name="brand", lookup_expr='iexact')
    brand_contains = filters.CharFilter(field_name="brand", lookup_expr='icontains')
    min_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='gte')
    max_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='lte')
    min_rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')
    released_after = filters.NumberFilter(field_name="created_at", lookup_expr='year__gte', help_text="year")

    class Meta:
        model = Product
        fields = ['category__name',
                  'name', 'name_contains',
                  'min_price', 'max_price',
                  'min_quantity', 'max_quantity',
                  'brand', 'brand_contains',
                  'released_after']


class CartItemFilter(filters.FilterSet):
    product__name = filters.CharFilter(lookup_expr='iexact')
    cart__user__username = filters.CharFilter(lookup_expr='iexact')
    min_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='gte')
    max_quantity = filters.NumberFilter(field_name="quantity", lookup_expr='lte')

    class Meta:
        model = CartItem
        fields = ['product__name', 'cart__user__username',
                  'min_quantity', 'max_quantity',
                 ]


class CartFilter(filters.FilterSet):
    user__user__username = filters.CharFilter(lookup_expr='iexact')
    completed = filters.BooleanFilter(lookup_expr='iexact', help_text="True/False")
    min_count = filters.NumberFilter(field_name="count", lookup_expr='gte')
    max_count = filters.NumberFilter(field_name="count", lookup_expr='lte')

    class Meta:
        model = Cart
        fields = ['user__user__username', 'completed',
                  'min_count', 'max_count',
                 ]


class CategoryFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="name", lookup_expr='iexact')
    category_contains = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['category', 'category_contains',
                 ]
