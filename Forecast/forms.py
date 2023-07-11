from django import forms

DETAIL_CHOICES = [
    ('current', 'Current Weather'),
    ('three-hour', '3-Hour Forecast 5 Days'),
    ('hourly', 'Hourly Forecast 4 days'),
    ('daily', 'Daily Forecast 16 days'),
    ('climate', 'Climatic Forecast 30 day'),
]

class WeatherForecastForm(forms.Form):
    latitude = forms.FloatField(widget=forms.NumberInput(attrs={"class": "form-control form-control-lg custom-field", "placeholder": "Latitude"}))
    longitude = forms.FloatField(widget=forms.NumberInput(attrs={"class": "form-control form-control-lg custom-field", "placeholder": "Longitude"}))
    detail = forms.ChoiceField(choices=DETAIL_CHOICES, widget=forms.Select(attrs={"class": "form-control form-control-lg custom-field", "placeholder": "Detailing Type"}))
