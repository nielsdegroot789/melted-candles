from django.contrib import admin

from apps.products.inline_required import AtLeastOneRequiredInlineFormSet
from apps.products.models import Product, Variant


class VariantInline(admin.TabularInline):
    model = Variant
    formset = AtLeastOneRequiredInlineFormSet


class ProductAdmin(admin.ModelAdmin):
    inlines = [VariantInline]


admin.site.register(Product, ProductAdmin)
