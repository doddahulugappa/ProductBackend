from .models import Product, Category, Cart, CartItem
from rest_framework import serializers
from django.contrib.auth.models import User


# Serializers define the API representation.
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('get_category_name')

    def get_category_name(self, obj):
        if obj.category_id:
            return obj.category.name
        return ""

    class Meta:
        model = Product
        fields = ['name', 'category_name', 'brand', 'price', 'quantity', 'description', 'rating', 'image']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    cartitems = Cart.objects.all().prefetch_related("cartitems")

    class Meta:
        model = Cart
        fields = ['user', 'cartitems', 'count', 'total', 'updated', 'created', 'completed']


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()
    cart = CartSerializer()

    class Meta:
        model = CartItem
        fields = ['product', 'cart', 'quantity']
