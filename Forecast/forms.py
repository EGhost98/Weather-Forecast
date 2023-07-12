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
    appid = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control form-control-lg custom-field", "placeholder": "API Key For OpenWeather Map (Optional)"}))
    
    def clean(self):
        cleaned_data = super().clean()
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        if latitude is None or not (-90 <= latitude <= 90):
            self.add_error('latitude', 'Latitude must be between -90 and 90.')
        
        if longitude is None or not (-180 <= longitude <= 180):
            self.add_error('longitude', 'Longitude must be between -180 and 180.')