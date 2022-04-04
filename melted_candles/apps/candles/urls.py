from django.urls import path
from apps.candles.views import CandleList


urlpatterns = [
    path('candles/', CandleList)
]