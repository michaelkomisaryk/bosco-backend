from django import template

from products.models import Product

register = template.Library()


@register.filter
def uah(value):
    return f"{value} грн"


@register.simple_tag
def product_count():
    return Product.objects.count()
