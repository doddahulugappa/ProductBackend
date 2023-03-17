from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

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
        fields = ['name', 'category_name', 'brand', 'price', 'quantity', 'description', 'rating', 'category', 'image']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


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
    product = ProductSerializer(read_only=True)
    cart = CartSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['product', 'cart', 'quantity']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    repeat_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'repeat_password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
