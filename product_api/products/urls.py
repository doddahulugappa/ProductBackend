"""
directory_app URL Configuration

"""
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, CartViewSet, CartItemViewSet, UploadViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Products API",
        default_version="v1",
        description="APIs for the Product App",

    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Products', ProductViewSet)
router.register(r'Category', CategoryViewSet)
router.register(r'Carts', CartViewSet)
router.register(r'CartItems', CartItemViewSet)

ProductImage = UploadViewSet.as_view({'put': 'update'})



urlpatterns = [
    path('', include(router.urls)),
    path('Products/<int:pk>/image/', ProductImage, name='image_upload'),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
