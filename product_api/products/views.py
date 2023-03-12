from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import viewsets, parsers, renderers, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .filters import ProductFilter
from .serializer import ProductSerializer, CategorySerializer, ProductImageSerializer, CartSerializer, \
    CartItemSerializer
from .models import Product, Category, Cart, CartItem
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    ordering_fields = ['price']


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]


class CartViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend]


class CartItemViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    filter_backends = [DjangoFilterBackend]


class UploadViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    queryset = Product.objects.all()
    serializer_class = ProductImageSerializer

    @action(detail=False, methods=['put'])
    def post(self, request, **kwargs):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data.get('image')
            serializer.save(image=data)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



