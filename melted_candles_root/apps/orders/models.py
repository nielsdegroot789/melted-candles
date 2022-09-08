from django.db import models
from django.core.validators import RegexValidator

from apps.base.models import BaseModel
from apps.products.models import Product, Variant
from apps.orders.order_choices import ORDER_CHOICES, DEFAULT_STATUS
from apps.orders.payment_choices import PAYMENT_CHOICES


class Order(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    pickup_date = models.DateTimeField(null=True)
    total = models.IntegerField()
    status = models.CharField(
        max_length=1, choices=ORDER_CHOICES, default=DEFAULT_STATUS)
    payment_method = models.CharField(choices=PAYMENT_CHOICES, max_length=1)
    # TODO: check wat die regex juist doet en welk formaat dit moet zijn
    phone_message = 'Telefoonnummer moet in dit formaat zijn: 05999999999'
    phone_regex = RegexValidator(
        regex=r'^(05)\d{9}$',
        message=phone_message
    )

    phone = models.CharField(validators=[phone_regex], max_length=60,
                             null=True, blank=True)
    products = models.ManyToManyField(Product, through='Order_Product')

    def __str__(self):
        return self.first_name + "  " + self.last_name


class Order_Product(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(
        Variant, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=3, decimal_places=0)
