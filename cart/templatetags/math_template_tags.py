from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(price, quantity, *args, **kwargs):
    return int(price) * int(quantity)