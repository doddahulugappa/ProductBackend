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
    # filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    # filterset_fields = ['price', 'category__name','brand','created_at', 'rating']
    ordering_fields = ['price']

    @action(detail=True, methods=['PUT'])
    def image(self, request, pk=None):
        product = self.get_object()
        image_obj = product.image
        print(image_obj)
        serializer = ProductSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data.get('image')
            serializer.save(image=data)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



class UploadView(GenericAPIView):
    parser_classes = (parsers.FileUploadParser, parsers.MultiPartParser, parsers.FormParser)
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['image',]

    @action(detail=False, methods=['post'])
    def post(self, request, **kwargs):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data.get('image')
            # serializer.save(image=data)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



