from .models import Product, Category, Cart
from rest_framework import serializers
from django.contrib.auth.models import User


# Serializers define the API representation.
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'price', 'quantity', 'description', 'rating']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'count', 'total', 'updated', 'timestamp']
