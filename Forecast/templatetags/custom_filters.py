from django import template
import datetime

register = template.Library()

@register.filter
def unix_to_datetime(unix_time):
    return datetime.datetime.fromtimestamp(unix_time)


@register.filter
def kev_cel(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)