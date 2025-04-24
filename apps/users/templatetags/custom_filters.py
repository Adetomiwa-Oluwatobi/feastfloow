from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """Generate a range of numbers from 1 to value."""
    return range(1, value + 1)

@register.filter
def inverse_range(value):
    """Generate a range of numbers from value + 1 to 5."""
    return range(value + 1, 6)
