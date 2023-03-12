from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, parsers, renderers, status
from rest_framework.decorators import action

from .filters import ProductFilter
from .serializer import ProductSerializer, CategorySerializer, ProductImageSerializer, CartSerializer, \
    CartItemSerializer
from .models import Product, Category, Cart, CartItem
from rest_framework.response import Response


# ViewSets define the view behavior.
from .utils.imageprocessing import start_parallel_processing


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

    @action(detail=True, methods=['put'])
    def update(self, request, pk=None):
        prod_obj = Product.objects.get(pk=pk)
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            image = serializer.validated_data.get('image')
            prod_obj.image=image
            prod_obj.save()
            try:
                start_parallel_processing([prod_obj.image.path])
            except Exception as e:
                print(e)

            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



