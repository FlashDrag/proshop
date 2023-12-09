from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView,
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import UserSerializer


@extend_schema(
    summary="Get tokens and user details",
    responses={
        (200, "application/json"): {
            "description": "JSON response",
            "type": "object",
            "properties": {
                "refresh": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 128,
                },
                "access": {"type": "string", "minLength": 1, "maxLength": 128},
                "id": {"type": "integer"},
                "_id": {"type": "integer"},
                "email": {"type": "string", "minLength": 1, "maxLength": 128},
                "name": {"type": "string", "minLength": 1, "maxLength": 128},
                "isAdmin": {"type": "boolean"},
                "token": {"type": "string", "minLength": 1, "maxLength": 128},
            },
        },
    },
)
class TokenObtainPairView(BaseTokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh
    JSON web token pair to prove the authentication of those credentials.
    Additionally, it returns the user details and a custom access token.
    """
    pass


@extend_schema(
    summary="User details",
    responses={200: OpenApiResponse(response=UserSerializer())},
)
@api_view(["GET"])
# @authentication_classes([JWTAuthentication]) - can be skipped as
# the JWTAuthentication class applied by default authentication
# for all views in settings/REST_FRAMEWORK
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    """User profile details"""
    user = request.user
    """
    # the same as @permission_classes([IsAuthenticated])
    if not user.is_authenticated:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    """
    serializer = UserSerializer(user)
    return Response(serializer.data)
