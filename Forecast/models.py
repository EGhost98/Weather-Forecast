from django.db import models


class WeatherForecast(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    detailing_type = models.CharField(max_length=20)
    weather_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['latitude', 'longitude', 'detailing_type']

    def __str__(self):
        return f'{self.latitude}, {self.longitude} ({self.detailing_type})'
