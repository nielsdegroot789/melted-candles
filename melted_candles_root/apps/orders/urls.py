from django.urls import path
from apps.orders.views import CreateOrder


urlpatterns = [
    path('create', CreateOrder.as_view()),
]
