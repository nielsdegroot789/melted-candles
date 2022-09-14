
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.orders.serializers import CreateOrderSerializer, OrderSerializer
from apps.orders.order_mail import send_order_emails
from apps.orders.stripe import create_stripe_checkout


class CreateOrder(APIView):
    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            order = OrderSerializer(obj).data
        if order["payment_method"] == 2:
            checkout_url = create_stripe_checkout(order)
            return Response(checkout_url, status=status.HTTP_201_CREATED)
        send_order_emails(order)
        return Response(status=status.HTTP_201_CREATED)

       
