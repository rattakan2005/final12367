from django import template

register = template.Library()

@register.filter
def floatformat(value, decimal_places=2):
    try:
        return f"{float(value):.{decimal_places}f}"
    except (ValueError, TypeError):
        return value