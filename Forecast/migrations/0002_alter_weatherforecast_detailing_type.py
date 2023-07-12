# Generated by Django 4.2.3 on 2023-07-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forecast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherforecast',
            name='detailing_type',
            field=models.CharField(choices=[('current', 'Current Weather'), ('three-hour', '3-Hour Forecast 5 Days'), ('hourly', 'Hourly Forecast 4 days'), ('daily', 'Daily Forecast 16 days'), ('climate', 'Climatic Forecast 30 day')], max_length=20),
        ),
    ]