from rest_framework import serializers
from apps.products.models import Product, Variant
class OrderSerializer(serializers.Serializer):
    product = serializers.IntegerField(write_only=True)
    variant = serializers.IntegerField(write_only=True)
    amount = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        try:
            Product.objects.get(id=validated_data.get('product'))
            Variant.objects.get(id=validated_data.get('variant'), product=validated_data.get('product'))
        except Exception as e:
            raise e
        return validated_data
