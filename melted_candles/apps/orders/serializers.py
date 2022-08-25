from rest_framework import serializers
from apps.products.models import Product, Variant
from apps.orders.models import Order, Order_Product


class OrderProductSerializer(serializers.Serializer):
    product = serializers.IntegerField(write_only=True)
    variant = serializers.IntegerField(write_only=True)
    amount = serializers.IntegerField(write_only=True)

    def validate_product(self, product):
        try:
            Product.objects.get(id=product)
        except Exception as e:
            print("errorrr")
            raise e
        return product

    def validate_variant(self, variant):
        try:
            Variant.objects.get(id=variant)
        except Exception as e:
            print("errorrr")
            raise e
        return variant

    def validate(self, data):
        try:
            Variant.objects.get(id=data.get("variant"),
                                product=data.get("product"))
        except Exception as e:
            raise e
        return data

    def create(self, validated_data):
        pass

    def update(self, obj, validated_data):
        pass


class OrderUserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    address = serializers.CharField()
    pickup_date = serializers.DateTimeField()
    phone = serializers.CharField()
    total = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, obj, validated_data):
        pass


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.Serializer):
    products = OrderProductSerializer(many=True, write_only=True)
    user = OrderUserSerializer(write_only=True)
    payment_method = serializers.CharField(write_only=True)

    def create(self, validated_data):
        order = Order.objects.create(
            email=validated_data['user']['email'],
            address=validated_data['user']['address'],
            total=validated_data['user']['total'],
            pickup_date=validated_data['user']['pickup_date'],
            phone=validated_data['user']['phone'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name'],
            payment_method=validated_data['payment_method']
        )
        for product in validated_data['products']:
            Order_Product.objects.create(
                product_id=product['product'],
                variant_id=product['variant'],
                amount=product['amount'],
                order=order
            )
        return order

    def update(self, obj, validated_data):
        pass
