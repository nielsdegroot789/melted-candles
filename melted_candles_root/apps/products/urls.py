from django.urls import path
from apps.products.views import ProductList


urlpatterns = [
    path('list', ProductList.as_view())
]