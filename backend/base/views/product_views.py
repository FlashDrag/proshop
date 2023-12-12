from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse

from base.models import Product
from base.serializers import ProductSerializer


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
    product = Product.objects.get_(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


"""
# OpenApi response example
@extend_schema(
    summary="API Routes",
    responses={
        200: OpenApiResponse(
            response={'type': 'array', 'items': {'type': 'string'}}
            # e.g. ["string"]
        )
    },
)
"""
