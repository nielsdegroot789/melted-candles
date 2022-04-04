from django.contrib import admin

from apps.candles.models import Candle

class CandleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Candle, CandleAdmin)