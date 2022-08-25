
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.orders.serializers import CreateOrderSerializer, OrderSerializer
from apps.orders.payment_choices import PAYMENT_CHOICES
from django.conf import settings
from apps.orders.models import Order_Product
from apps.products.models import Product
from helpers.numbers import integer_with_point_to_decimal
import stripe
from django.core.mail import send_mail


class CreateOrder(APIView):
    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            order = OrderSerializer(obj).data
        if order["payment_method"] == 2:
            checkout_url = createStripeCheckout(order)
            return Response(checkout_url, status=status.HTTP_201_CREATED)
        createCheckout(order)
        return Response(status=status.HTTP_201_CREATED)

        #  TODO: give images to api
        # https://stripe.com/docs/api/products/object


def createCheckout(order):
    order_products = Order_Product.objects.filter(order=order["id"]).values()

    begin_message = f"Hey Elien, \n Er is zojuist een bestelling geplaatst door {order['first_name']} {order['last_name']}: \n\n"
    for order_product in order_products:
        product = Product.objects.get(id=order_product["product_id"])
        product_message += f"{order_product['amount']}x {product} \n"

    message = begin_message + product_message + \
        f"\n Email: {order['email']} \n\n Nog een fijne dag gewenst broow \n groetjes de webshop"

    send_mail(
        subject='Aankoop kaarsen',
        message=message,
        from_email='noreply@gmail.com',
        recipient_list=['nielsdegroot@live.be', ],
        fail_silently=False,
    )


def createStripeCheckout(order):
    order_products = Order_Product.objects.filter(order=order["id"]).values()
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    begin_message = f"Hey Elien, \n Er is zojuist een bestelling geplaatst door {order['first_name']} {order['last_name']}: \n\n"
    stripe_products = []
    product_message = ""

    for order_product in order_products:
        product = Product.objects.get(id=order_product["product_id"])
        stripe_product = {
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': product,
                },
                'unit_amount': integer_with_point_to_decimal(product.price),
            },
            'quantity': order_product["amount"],
        }

        product_message += f"{order_product['amount']}x {product} \n"
        stripe_products.append(stripe_product)

    try:
        message = begin_message + product_message + \
            f"\n Email: {order['email']} \n\n Nog een fijne dag gewenst broow \n groetjes de webshop"
        session = stripe.checkout.Session.create(
            line_items=stripe_products,
            mode='payment',
            success_url='http://localhost:4242/success.html',
            cancel_url='http://localhost:4242/cancel.html',
        )

        send_mail(
            subject='Aankoop kaarsen',
            message=message,
            from_email='noreply@gmail.com',
            recipient_list=['nielsdegroot@live.be', ],
            fail_silently=False,
        )

    except Exception as e:
        print(e)
    return session.url
