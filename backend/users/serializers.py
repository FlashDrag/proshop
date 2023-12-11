from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    # create custom fields for the serializer
    # read_only=True means that the field is not required in the request
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "_id", "email", "name", "isAdmin"]

    def get__id(self, obj) -> int:
        """
        Set the value of the custom '_id' field to the value of the 'id' field.
        The method name must be get_<field_name>"""
        return obj.id

    def get_isAdmin(self, obj) -> bool:
        """
        Set the value of the custom 'isAdmin' field to the value
        of the 'is_staff' field.
        """
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    """
    Extends the UserSerializer class to add a custom access 'token' field.
    Also used to create a new user. Use it in the registerUser view.
    """
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "_id", "email", "password", "name", "isAdmin", "token"]
        # set the password field to write only, so that users can't see
        # the password in the response
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def get_token(self, obj):
        """
        Set the value of the custom 'token' field to the value
        """
        # generate a new refresh and access token for
        # the obj(which is a existing user)
        token = RefreshToken.for_user(obj)
        # return the access token
        return str(token.access_token)

    def create(self, validated_data):
        """Create and return a new user with encrypted password"""
        user = get_user_model().objects.create_user(**validated_data)
        return user


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
