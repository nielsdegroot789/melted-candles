
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.orders.serializers import OrderSerializer

class CreateOrder(APIView):

    def post(self, request):
        print('data', request.data)
        serializer = OrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            print("valid")
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
 