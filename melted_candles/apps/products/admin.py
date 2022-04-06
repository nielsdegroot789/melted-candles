from django.contrib import admin

from apps.products.models import Product, Variant
class VariantInline(admin.TabularInline):
    model = Variant
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines =  [VariantInline]

   
admin.site.register(Product, ProductAdmin)