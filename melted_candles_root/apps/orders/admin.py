from django.contrib import admin

from apps.orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)