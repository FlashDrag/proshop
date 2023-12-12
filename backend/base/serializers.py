from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # create custom fields for the serializer instead
    # of python convention field names like 'num_reviews'
    numReviews = serializers.SerializerMethodField()
    countInStock = serializers.SerializerMethodField()
    createdAt = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ("num_reviews",  "count_in_stock", "created_at", "user")

    def get_numReviews(self, obj) -> int:
        return obj.num_reviews

    def get_countInStock(self, obj) -> int:
        return obj.count_in_stock

    def get_createdAt(self, obj):
        return obj.created_at
