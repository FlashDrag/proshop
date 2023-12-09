from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["email"] = self.user.email

        return data


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
