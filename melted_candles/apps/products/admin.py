from django.contrib import admin
import admin_thumbnails

from apps.products.inline_required import AtLeastOneRequiredInlineFormSet
from apps.products.models import Product, Variant


class VariantInline(admin.TabularInline):
    model = Variant
    formset = AtLeastOneRequiredInlineFormSet


@admin_thumbnails.thumbnail('picture')
class ProductAdmin(admin.ModelAdmin):
    inlines = [VariantInline]


admin.site.register(Product, ProductAdmin)
