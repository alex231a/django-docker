"""
API views for exposing product catalogue data.

Provides a viewset that allows read-only access to the product list
and detail endpoints via the Django REST Framework.
"""

import logging
from rest_framework import viewsets
from oscar.apps.catalogue.models import Product # pylint: disable=import-error
from .serializers import ProductSerializer

logger = logging.getLogger('shop_api')

class ProductViewSet(viewsets.ReadOnlyModelViewSet):# pylint: disable=too-many-ancestors
    """
    A viewset that provides read-only access to Product resources.

    This viewset supports:
    - Listing all products (GET /api/products/)
    - Retrieving a specific product by ID (GET /api/products/{id}/)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        logger.info(f"[ProductViewSet:list] User {request.user} requested product list")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        logger.info(f"[ProductViewSet:retrieve] User {request.user} requested product ID {product_id}")
        return super().retrieve(request, *args, **kwargs)
