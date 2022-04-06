from django.db import models
from django.core.validators import RegexValidator

from apps.base.models import BaseModel
from apps.orders.order_choices import ORDER_CHOICES, DEFAULT_STATUS

class Order(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    phone_message = 'Telefoonnummer moet in dit formaat zijn: 05999999999' 
    phone_regex = RegexValidator(
        regex=r'^(05)\d{9}$',
        message=phone_message
    )

    phone = models.CharField(validators=[phone_regex], max_length=60,
                             null=True, blank=True)
    address = models.CharField(max_length=100)
    pickup_date = models.DateTimeField()
    total = models.IntegerField()
    status = models.CharField(max_length=1, choices=ORDER_CHOICES, default=DEFAULT_STATUS)
