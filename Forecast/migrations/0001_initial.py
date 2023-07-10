# Generated by Django 4.2.3 on 2023-07-10 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('detailing_type', models.CharField(max_length=20)),
                ('weather_data', models.JSONField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('latitude', 'longitude', 'detailing_type')},
            },
        ),
    ]