from django.urls import path
from apps.products.views import ProductList


urlpatterns = [
    path('products/', ProductList.as_view())
]