from django.db import models

class WeatherForecast(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    DETAIL_CHOICES = [
        ('current', 'Current Weather'),
        ('three-hour', '3-Hour Forecast 5 Days'),
        ('hourly', 'Hourly Forecast 4 days'),
        ('daily', 'Daily Forecast 16 days'),
        ('climate', 'Climatic Forecast 30 day'),
    ]
    detailing_type = models.CharField(max_length=20, choices=DETAIL_CHOICES)
    weather_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['latitude', 'longitude', 'detailing_type']

    def __str__(self):
        return f'{self.latitude}, {self.longitude} ({self.detailing_type})'
