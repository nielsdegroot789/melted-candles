from django.db import models

from apps.base.models import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.ImageField(upload_to='products')
    # TODO: https://ilovedjango.com/django/admin/how-to-show-image-from-imagefield-in-django-admin-page/
    # manage files with django https://docs.djangoproject.com/en/4.0/topics/files/
    def __str__(self):
        return self.name