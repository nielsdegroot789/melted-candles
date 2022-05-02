
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.orders.serializers import CreateOrderSerializer, OrderSerializer

class CreateOrder(APIView):

    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(OrderSerializer(obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
 