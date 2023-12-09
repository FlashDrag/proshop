from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    # create custom fields for the serializer
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "_id", "email", "name", "isAdmin"]

    def get__id(self, obj):
        """
        Set the value of the custom '_id' field to the value of the 'id' field.
        The method name must be get_<field_name>"""
        return obj.id

    def get_isAdmin(self, obj):
        """
        Set the value of the custom 'isAdmin' field to the value
        of the 'is_staff' field.
        """
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    """
    Extends the UserSerializer class to add a custom access 'token' field
    """
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "_id", "email", "name", "isAdmin", "token"]

    def get_token(self, obj):
        """
        Set the value of the custom 'token' field to the value
        """
        # generate a new refresh and access token for
        # the obj(which is a existing user)
        token = RefreshToken.for_user(obj)
        # return the access token
        return str(token.access_token)


# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Override the default TokenObtainPairSerializer
    to add custom claims from the UserSerializerWithToken
    to the payload.

    In client side, we can get the "access" or "token" key from the payload
    data, as they both are access tokens and are interchangeable.
    """
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        # Simple example of custom claim without a UserSerializer
        # data["email"] = self.user.email

        return data
