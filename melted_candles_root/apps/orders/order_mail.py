
from django.core.mail import send_mail
from apps.orders.models import Order_Product
from apps.products.models import Product


def send_order_emails(order):
    send_confirm_email_to_client(order)
    send_confirm_mail_to_owner(order)


def send_confirm_email_to_client(order):

    begin_message = f"Hey dag {order['first_name']}, \n Bedankt voor de bestelling bij Melted Candles. \n\n Jouw kaarsen worden zo snel mogelijk opgestuurd om je interieur nog mooier te maken.\n"

    product_message = get_ordered_products_text(order['id'])
    end_message = f"\n\n Nog een fijne dag gewenst! \n Groetjes Elien"

    send_mail(
        subject='Bevestiging bestelling kaarsen',
        message=begin_message + product_message + end_message,
        from_email='noreply@gmail.com',
        recipient_list=[order['email']],
        fail_silently=False,
    )


def send_confirm_mail_to_owner(order):

    begin_message = f"Hey Elien, \n Er is zojuist een bestelling geplaatst door {order['first_name']} {order['last_name']}: \n\n"
    product_message = get_ordered_products_text(order["id"])

    message = begin_message + product_message + \
        f"\n Email: {order['email']} \n\n Nog een fijne dag gewenst broow \n groetjes de webshop"

    send_mail(
        subject='Aankoop kaarsen',
        message=message,
        from_email='noreply@gmail.com',
        recipient_list=['nielsdegroot@live.be', ],
        fail_silently=False,
    )


def get_ordered_products_text(order_id):
    order_products = Order_Product.objects.filter(order=order_id).values()
    product_message = ""

    for order_product in order_products:
        product = Product.objects.get(id=order_product["product_id"])
        product_message += f"{order_product['amount']}x {product} \n"

    return product_message
