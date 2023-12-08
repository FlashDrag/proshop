from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import UserSerializer


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
    '''
    # the same as @permission_classes([IsAuthenticated])
    if not user.is_authenticated:
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    '''
    serializer = UserSerializer(user)
    return Response(serializer.data)
