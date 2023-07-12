from django import template
import datetime

register = template.Library()

@register.filter
def unix_to_datetime(unix_time):
    datetime_obj = datetime.datetime.fromtimestamp(unix_time)
    formatted_datetime = datetime_obj.strftime("%I:%M %p, %b %d, %A")  # Format the datetime
    return formatted_datetime



@register.filter
def kev_cel(kelvin):
    celsius = kelvin - 273.15
    return round(celsius)