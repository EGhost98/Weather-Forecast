from django import forms

DETAIL_CHOICES = [
    ('current', 'Current Weather'),
    ('three-hour', '3-Hour ForeCast 5 Days'),
    ('hourly', 'Hourly Forecast 4 days'),
    ('daily', 'Daily Forecast 16 days'),
    ('climate', 'Climatic Forecast 30 day'),
]

class WeatherForecastForm(forms.Form):
    latitude = forms.FloatField(label='Latitude')
    longitude = forms.FloatField(label='Longitude')
    detail = forms.ChoiceField(choices=DETAIL_CHOICES, label='Detailing Type')
