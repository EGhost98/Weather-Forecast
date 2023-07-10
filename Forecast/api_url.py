def get_api_url(detail, api_key, lat, lon):
    api_url = ""

    switch = {
        'current': lambda: f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}',
        'three-hour': lambda: f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}',
        'hourly': lambda: f'https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}',
        'daily': lambda: f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&appid={api_key}',
        'climate': lambda: f'https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={api_key}'
    }

    api_url = switch.get(detail, lambda: None)()

    return api_url
