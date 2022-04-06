from apps.base.models import BaseModel
from colorfield.fields import ColorField

class VariantModel(BaseModel):
    color = ColorField(default='#FF0000')