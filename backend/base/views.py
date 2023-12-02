from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .models import Product
from .serializers import ProductSerializer


@extend_schema(
    summary="API Routes",
    responses={
        200: OpenApiResponse(
            response={'type': 'array', 'items': {'type': 'string'}},
        )
    },
)
@api_view(["GET"])
def getRoutes(request):
    """List of all routes"""
    routes = [
        "/api/products/",
        "/api/products/create/",
        "/api/products/upload/",
        "/api/products/<id>/reviews/",
        "/api/products/top/",
        "/api/products/<id>/",
        "/api/products/delete/<id>/",
        "/api/products/<update>/<id>/",
    ]
    return Response(routes)


@extend_schema(
    summary="Products list",
    responses={200: OpenApiResponse(response=ProductSerializer(many=True))},
)
@api_view(["GET"])
def getProducts(request):
    """List of all products"""
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@extend_schema(
    summary="Product details",
    responses={200: OpenApiResponse(response=ProductSerializer)},
)
@api_view(["GET"])
def getProduct(request, pk):
    """Product details"""
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
