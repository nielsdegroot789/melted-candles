from django.db import models

from apps.base.models import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    picture = models.ImageField()

    def __str__(self):
        return self.name