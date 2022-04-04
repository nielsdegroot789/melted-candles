
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.candles.models import Candle
from apps.candles.serializers import CandleSerializer


class CandleList(APIView):
    def get(self, request):
        candles = Candle.Objects.all()
        serializer = CandleSerializer(candles)
        print(serializer.data, 'hallo')
        return Response(serializer.data)