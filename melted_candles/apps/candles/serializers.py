from rest_framework import serializers

from apps.candles.models import Candle


class CandleSerializer(serializers.ModelSerializer):
    model = Candle
    fields = '__all__'