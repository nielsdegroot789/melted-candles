from django.db import models
from core.models import BaseModel

class Candle(BaseModel):
    name: models.CharField(max_length=100)
    description: models.TextField()
    price: models.DecimalField()
    picture: models.ImageField()
    
    def __str__(self):
        return self.title