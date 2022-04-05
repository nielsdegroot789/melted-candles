
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductList(APIView):
    def get(self, request):
        candles = Product.Objects.all()
        serializer = ProductSerializer(candles)
        print(serializer.data, 'hallo')
        return Response(serializer.data)