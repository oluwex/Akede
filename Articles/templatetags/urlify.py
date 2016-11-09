from urllib.parse import quote_plus
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def urlify(text):
    return quote_plus(text)