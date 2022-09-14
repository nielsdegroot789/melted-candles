from django.conf import settings
from apps.orders.models import Order_Product
from apps.products.models import Product
from helpers.numbers import integer_with_point_to_decimal
from apps.orders.order_mail import send_order_emails
import stripe

#  TODO: give images to api
# https://stripe.com/docs/api/products/object
#  TODO: create stripe abstract interface

def create_stripe_checkout(order):
    order_products = Order_Product.objects.filter(order=order["id"]).values()
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    stripe_products = []

    send_order_emails(order)

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

        stripe_products.append(stripe_product)

    try:
        session = stripe.checkout.Session.create(
            line_items=stripe_products,
            mode='payment',
            success_url='http://localhost:4242/success.html',
            cancel_url='http://localhost:4242/cancel.html',
        )

    except Exception as e:
        print(e)
    return session.url
